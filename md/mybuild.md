[mac]
python3 -m venv venv
source venv/bin/activate
python app.py

[windows]
python -m venv venv
venv\Scripts\activate
python app.py



http://127.0.0.1:5000

http://127.0.0.1:5000/shuffle

http://127.0.0.1:5000/confirm?page_num=1

http://127.0.0.1:5000/confirm?page_num=2

http://127.0.0.1:5000/confirm?page_num=3

http://127.0.0.1:5000/guests

http://127.0.0.1:5000/attend

http://127.0.0.1:5000/prize

http://127.0.0.1:5000/screen

http://127.0.0.1:5000/winners


git init
git remote add origin https://github.com/tztechno/vercel_flask_party.git
git pull origin master 
git add .
git commit -m "2024-10-26"
git push -u origin master
git push -f origin master


祝賀会_project/
│
├── app.py                   # Flaskアプリケーションのメインファイル
│
├── sources/                 # データソースのディレクトリ
│   ├── prize.csv            # あらかじめ作成しておく
│   ├── guests.csv           # あらかじめ作成しておく
│   ├── attend.csv           # 受付QRコード読み取り結果を出力したものを置く
│   └── winners.csv          # 採用する受賞者リストを置く
│
├── templates/               # HTMLテンプレートのディレクトリ
│   ├── index.html
│   ├── shuffle.html
│   └── ...                  # 他のテンプレート

