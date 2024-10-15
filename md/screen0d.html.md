<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Screen</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
            background-image: url('sakura01.gif');
            /* ここを修正 */
            background-size: cover;
            /* 画面全体に背景を表示 */
            background-repeat: no-repeat;
            /* 繰り返さない */
            background-position: center;
            /* 中央に配置 */
        }

        iframe {
            width: 96%;
            height: 96%;
            border: none;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            background-color: transparent;
            /* iframeの背景を透明に設定 */
        }
    </style>
</head>

<body>

    <iframe id="screen-frame" src="{{ current_page }}"></iframe> <!-- ここを修正 -->

    <script>
        // 現在のページを取得する関数
        function getCurrentPage() {
            fetch('/get_current_page')
                .then(response => response.json())
                .then(data => {
                    document.getElementById("screen-frame").src = data.current_page;  // src を修正
                })
                .catch(error => console.error('Error:', error));
        }

        // ページ読み込み時に現在のページを取得
        getCurrentPage();

        // 5秒ごとに現在のページを確認し、更新
        setInterval(getCurrentPage, 2000);
    </script>
</body>

</html>