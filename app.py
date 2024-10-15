from flask import Flask, render_template, jsonify
from flask import redirect, url_for, send_from_directory
from flask import request, session
import csv
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'
saved_winners = []

def load_csv_files():
    try:
        prize_df = load_csv('sources/prize.csv')
        guests_df = load_csv('sources/guests.csv')
        attend_df = load_csv('sources/attend.csv')
        return prize_df, guests_df, attend_df
    except Exception as e:
        print(f"Error loading CSV files: {e}")
        return [], [], []  # 空のリストを返す

def load_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qr_read')
def qr_read():
    return render_template('qr_read.html')


@app.route('/shuffle')
def shuffle():
    global saved_winners  # 既存の受賞者データをリセット
    saved_winners = []

    prize_df, guests_df, attend_df = load_csv_files()

    prizes = []
    for row in prize_df:
        prizes.extend([row['prize']] * int(row['n']))

    attendid = [row['id'] for row in attend_df]
    random.shuffle(attendid)

    for i in range(len(prizes)):
        idi = attendid[i]
        attendee = next((row for row in guests_df if row['id'] == idi), None)

        if attendee is None:
            continue
        
        winner = {
            'prize': prizes[i],
            'id': attendee['id'],
            'comp': attendee['comp'],
            'name': attendee['name'],
        }
        saved_winners.append(winner)  # グローバルに保存

    return render_template('shuffle.html', winners=saved_winners)


@app.route('/confirm', methods=['POST', 'GET'])
def confirm():
    global saved_winners

    if request.method == 'POST':
        return redirect(url_for('confirm', page_num=1))  # 受賞者を確認後、最初のページにリダイレクト

    prizes = list(set([winner['prize'] for winner in saved_winners]))
    prizes.sort()  # 賞のソート

    # 1ページに表示する賞の数（賞ごとにページを分ける）
    PER_PAGE = 1
    total_pages = len(prizes)

    page_num = request.args.get('page_num', default=1, type=int)

    if page_num < 1 or page_num > total_pages:
        return "Page not found", 404

    # 現在のページの賞に対応する受賞者を抽出
    current_prize = prizes[page_num - 1]
    paginated_winners = [winner for winner in saved_winners if winner['prize'] == current_prize]

    confirm_time = session.get('confirm_time', None)

    return render_template('confirm.html', winners=paginated_winners, current_prize=current_prize, page_num=page_num, total_pages=total_pages, confirm_time=confirm_time)

# /guests ルート：ゲストリストを表示
@app.route('/guests')
def display_guests():
    guests_df = load_csv('sources/guests.csv')
    return render_template('guests.html', guests=guests_df)

# /attend ルート：参加者リストを表示
@app.route('/attend')
def display_attendees():
    guests_df = load_csv('sources/guests.csv')
    attend_df = load_csv('sources/attend.csv')
    attended_guests = [row for row in guests_df if row['id'] in [attendee['id'] for attendee in attend_df]]
    return render_template('attend.html', guests=attended_guests)

# /prize ルート：賞リストを表示
@app.route('/prize')
def display_prizes():
    prize_df = load_csv('sources/prize.csv')
    return render_template('prize.html', prizes=prize_df)

# サンプルのページリスト
selectable_pages = ['/prize', '/attend', '/confirm?page_num=1', '/confirm?page_num=2', '/confirm?page_num=3']
current_page = '/prize'

nickname_map = {
'/prize':'賞品', 
'/attend':'本日の参加者', 
'/confirm?page_num=1':'Z1', 
'/confirm?page_num=2':'Z2',
'/confirm?page_num=3':'Z3'
}

@app.route('/screen')
def screen():
    return render_template('screen.html', selectable_pages=selectable_pages, current_page=current_page, nickname_map=nickname_map)

@app.route('/set_current_page', methods=['POST'])
def set_current_page():
    global current_page
    page = request.json.get('page')
    if page in selectable_pages:
        current_page = page
        return jsonify({'success': True, 'current_page': current_page})
    else:
        return jsonify({'success': False}), 400

@app.route('/get_current_page', methods=['GET'])
def get_current_page():
    return jsonify({'current_page': current_page})

if __name__ == '__main__':
    app.run(debug=True)
