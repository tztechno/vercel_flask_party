
---

# 管理者アプリ

---
<br>

- 管理者用DEMOアプリ: [https://vercel-flask-party.vercel.app/](https://vercel-flask-party.vercel.app/) 

- 本番では、PCに設置して使用します（非公開）。 

###  賞品
- sources/prize.csvを読み込み表示します

###  招待者一覧
- sources/guests.csvを読み込み表示します

### 本日の参加者
- sources/attend.csvのidに、guests.csvの所属、氏名をマージして表示します。

- today_attend.csvとして出力可能です。

### 抽選
- 賞品の抽選を当選者数に従って一括実施可能（必要なければ使わなくても良い）。結果は,winners.csvとして出力可能です。

### 受賞者一覧
- 決定した抽選結果sources/winners.csvを読み込み表示します。

### 賞別受賞者
- 賞別にwinnersを表示します。

### 受付
- QRリーダー。端末ごとにattend.csvとして出力可能です。

- 受付終了後に統合されたattend.csvをsourcesフォルダに置きます。

### お知らせ
- 任意のテキストをスクリーンに表示できるようにしました。お知らせページの下にtextareaがあり、そこに入力されたものがそのまま表示されます。

- 緊急のお知らせを表示したい場合に利用可能です。（必要なければ使わなくても良い）

### フロア図
- 会場のフロア図を表示できます（現在はサンプル図）。マウスで図の拡大縮小移動が可能になっています。

### Sound
- 設置したmp3ファイルについてアイコンを表示し、soundを鳴らすことが出来ます。ドラム音３種類登録済み。他にも使いたい効果音があれば追加登録できます。

### Manual
- このDocumentです。

- md/manual.mdの内容を表示します。

### Screen
- Screenにはこのページだけを表示させます。下側にボタンが並んでおり、表示を切り替えることが出来ます。

- 現在の設置ページ：賞品、本日の参加者、賞別受賞者、お知らせ、フロア図

<br><br><br><br>

---

# QR発行サイト

---
<br>

- QR発行DEMOサイト: [https://vercel-flask-party-qr.vercel.app/](https://vercel-flask-party-qr.vercel.app/)

- 招待者がアクセスする公開サイトになります。

- 本番までに、主催者所有のサイトを立ち上げることが必要です。主催者所有のGitHubに置いて、Vercelなどにデプロイして公開します。

- QR表示には登録氏名と入力氏名が完全一致する必要があります。そのためには、同姓同名の存在、苗字名前の間の空白の有無、旧漢字か新漢字か（斎藤、齋藤）、ひらがらの大小（よ、ょ）、などの問題が無いことが必要です。

- この問題を回避するには、招待メールでIDを知らせて、QR取得時の入力にIDも使用可能にしておくことも一案です。ご検討ください。

- TOPページをPWを入力ページにすることも可能です。この設定を希望される場合は、お知らせください。（招待者にあらかじめPWを知らせる必要があります）（TOPページ=PW入力ページ—>招待者情報入力ページ—>QR表示ページ、の順に開きます）

<br><br><br><br>

---

# QRコードreader

---
<br>

- QRコードreader DEMO URL: [https://vercel-party-qr-reader.vercel.app/](https://vercel-party-qr-reader.vercel.app/)

- 本機能だけを切り出したURLを準備するとスマホでQRコードの読み取りが実施可能です。

- 本番までに、主催者所有GitHubに取り込みGitHub PagesまたはVercelなどに設置する必要があります。

- 受付に使うQRコードreaderは、重複する読み取り結果を表示しないようにしました。

- 使用端末からはattend.csvというファイル名で出力されます。

- 複数の端末でreaderを使う場合は、出力ファイルを合体する必要があります。

<br><br><br><br>

---

<br><br><br><br><br>
