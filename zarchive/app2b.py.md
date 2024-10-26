from flask import Flask, render_template, jsonify
from flask import redirect, url_for, send_from_directory
from flask import request, session 
import csv
import random
import os

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
    with open(file_path, mode='r', encoding='utf-8-sig') as csvfile:
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


@app.route('/winners')
def winners():
    winners_data = []

    # CSVファイルを読み込む
    with open('sources/winners.csv', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            winners_data.append(row)
    print(winners_data)
    # テンプレートにデータを渡してレンダリング
    return render_template('winners.html', winners=winners_data)


@app.route('/shuffle')
def shuffle():
    global saved_winners  # 既存の受賞者データをリセット
    saved_winners = []

    prize_df, guests_df, attend_df = load_csv_files()

    prizes = []
    for row in prize_df:
        prizes.extend([row['prize_id']] * int(row['n']))

    attendid = [row['id'] for row in attend_df]
    random.shuffle(attendid)

    for i in range(len(prizes)):
        idi = attendid[i]
        attendee = next((row for row in guests_df if row['id'] == idi), None)

        if attendee is None:
            continue
        
        winner = {
            'prize_id': prizes[i],
            'id': attendee['id'],
            'comp': attendee['comp'],
            'name': attendee['name'],
        }
        saved_winners.append(winner)  # グローバルに保存

    return render_template('shuffle.html', winners=saved_winners)


def load_prizes():
    prize_mapp = {}
    with open('sources/prize.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            prize_mapp[row['prize_id']] = row['prize_name']  # prize_idをキー、prize_nameを値とする
    return prize_mapp


def load_winners():
    winners = []
    with open('sources/winners.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            winners.append(row)
    return winners



@app.route('/confirm', methods=['POST', 'GET'])
def confirm():
    global saved_winners
    saved_winners = load_winners()  # 受賞者をCSVから読み込む
    prize_mapp = load_prizes()  # 賞品データをCSVから読み込む

    if request.method == 'POST':
        return redirect(url_for('confirm', page_num=1))  # 受賞者を確認後、最初のページにリダイレクト

    prizes = list(set([winner['prize_id'] for winner in saved_winners]))
    prizes.sort()  # 賞のソート
    print(prizes)

    # 1ページに表示する賞の数（賞ごとにページを分ける）
    PER_PAGE = 1
    total_pages = len(prizes)

    page_num = request.args.get('page_num', default=1, type=int)

    if page_num < 1 or page_num > total_pages:
        return "Page not found", 404

    # 現在のページの賞に対応する受賞者を抽出
    current_prize = prizes[page_num - 1]
    paginated_winners = [winner for winner in saved_winners if winner['prize_id'] == current_prize]

    # prize_mappを使ってprize_nameを取得
    prize_name = prize_mapp.get(current_prize, "不明な賞")

    return render_template('confirm.html', winners=paginated_winners, current_prize=current_prize, prize_name=prize_name, page_num=page_num, total_pages=total_pages, prize_mapp=prize_mapp)



@app.route('/guests')
def display_guests():
    guests_df = load_csv('sources/guests.csv')
    return render_template('guests.html', guests=guests_df)


@app.route('/attend')
def display_attendees():
    guests_df = load_csv('sources/guests.csv')
    attend_df = load_csv('sources/attend.csv')
    attended_guests = [row for row in guests_df if row['id'] in [attendee['id'] for attendee in attend_df]]
    return render_template('attend.html', guests=attended_guests)


@app.route('/prize')
def display_prizes():
    prize_df = load_csv('sources/prize.csv')
    return render_template('prize.html', prizes=prize_df)

# サンプルのページリスト
selectable_pages = ['/prize', '/attend', '/confirm?page_num=1', '/confirm?page_num=2', '/confirm?page_num=3', '/confirm?page_num=4',]
current_page = '/prize'

nickname_map = {
'/prize':'賞品', 
'/attend':'本日の参加者', 
'/confirm?page_num=1':'Z1', 
'/confirm?page_num=2':'Z2',
'/confirm?page_num=3':'Z3',
'/confirm?page_num=4':'Z4', 

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

@app.route('/mp3_player')
def mp3_player():
    # static/mp3 フォルダにあるMP3ファイルを取得し、ソート
    mp3_folder = os.path.join(app.static_folder, 'mp3')
    mp3_files = sorted([f for f in os.listdir(mp3_folder) if f.endswith('.mp3')])

    # ソート済みファイル名リストをHTMLテンプレートに渡す
    return render_template('mp3_player.html', mp3_files=mp3_files)


if __name__ == '__main__':
    app.run(debug=True)
