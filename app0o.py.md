from flask import Flask, render_template, jsonify, redirect, url_for, send_from_directory, request, session
import csv
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# グローバル変数に受賞者データを保存
saved_winners = []

@app.route('/save-confirmation-time', methods=['POST'])
def save_confirmation_time():
    data = request.json
    session['confirm_time'] = data['confirmTime']  # セッションに保存
    return {'status': 'success'}

# CSVファイルの読み込み
def load_csv_files():
    try:
        prize_df = load_csv('sources/prize.csv')
        guests_df = load_csv('sources/guests.csv')
        attend_df = load_csv('sources/attend.csv')
        return prize_df, guests_df, attend_df
    except Exception as e:
        print(f"Error loading CSV files: {e}")
        return [], [], []  # 空のリストを返す

# CSVをリストとして読み込むヘルパー関数
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
    global saved_winners
    saved_winners = []

    prize_df, guests_df, attend_df = load_csv_files()

    prizes = []
    for row in prize_df:
        prizes.extend([row['prize']] * int(row['n']))

    attendid = [row['id'] for row in attend_df]
    random.shuffle(attendid)

    winners = []
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
        winners.append(winner)
        saved_winners.append(winner)

    return render_template('shuffle.html', winners=winners)

@app.route('/confirm', methods=['POST', 'GET'])
@app.route('/confirm/<int:page_num>', methods=['POST', 'GET'])
def confirm(page_num=1):
    global saved_winners

    if request.method == 'POST':
        confirmed_winners = []
        prize_list = request.form.getlist('prize')
        id_list = request.form.getlist('id')
        comp_list = request.form.getlist('comp')
        name_list = request.form.getlist('name')

        for prize, id, comp, name in zip(prize_list, id_list, comp_list, name_list):
            winner = {
                "prize": prize,
                "id": id,
                "comp": comp,
                "name": name
            }
            confirmed_winners.append(winner)

        saved_winners.extend(confirmed_winners)

    prizes = list(set([winner['prize'] for winner in saved_winners]))
    prizes.sort()

    PER_PAGE = 1
    total_pages = len(prizes)

    if page_num < 1 or page_num > total_pages:
        return "Page not found", 404

    current_prize = prizes[page_num - 1]
    paginated_winners = [winner for winner in saved_winners if winner['prize'] == current_prize]

    confirm_time = session.get('confirm_time', None)
    return render_template('confirm.html', winners=paginated_winners, current_prize=current_prize, page_num=page_num, total_pages=total_pages, confirm_time=confirm_time)

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

@app.route('/screen')
def screen():
    return render_template('screen.html')

# サンプルのページリスト
selectable_pages = ['/prize', '/attend', '/confirm/1', '/confirm/2', '/confirm/3']
current_page = '/prize'

@app.route('/screen_controller')
def screen_controller():
    return render_template('screen_controller.html', selectable_pages=selectable_pages, current_page=current_page)

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