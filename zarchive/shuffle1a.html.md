<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>抽選</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th,
        td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
        }

        .filter-container {
            margin-bottom: 20px;
        }

        .shuffle-link {
            margin-top: 20px;
            display: inline-block;
            padding: 10px 15px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }

        .shuffle-link:hover {
            background-color: #45a049;
        }
    </style>
    <script>
        // shuffleページでの確定ボタン処理
        document.getElementById('confirmShuffleButton').addEventListener('click', function () {
            const now = new Date();
            const formattedTime = now.toISOString(); // サーバーに送るためISOフォーマットに変換

            // 確定時刻をサーバーに送信
            fetch('/save-confirmation-time', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ confirmTime: formattedTime }),
            })
                .then(response => response.json())
                .then(data => {
                    console.log('サーバーに保存成功:', data);
                })
                .catch((error) => {
                    console.error('エラー:', error);
                });
        });

        function populatePrizeFilter() {
            var rows = document.querySelectorAll('tbody tr');
            var prizes = new Set();

            rows.forEach(function (row) {
                var prize = row.querySelector('td:first-child').textContent;
                prizes.add(prize);
            });

            var filterSelect = document.getElementById('prize-filter');
            prizes.forEach(function (prize) {
                var option = document.createElement('option');
                option.value = prize;
                option.textContent = prize;
                filterSelect.appendChild(option);
            });
        }

        function filterWinners() {
            var filter = document.getElementById('prize-filter').value;
            var rows = document.querySelectorAll('tbody tr');

            rows.forEach(function (row) {
                var prize = row.querySelector('td:first-child').textContent;
                if (filter === "" || prize === filter) {
                    row.style.display = "";
                } else {
                    row.style.display = "none";
                }
            });
        }

        window.onload = function () {
            populatePrizeFilter();
        };
    </script>
</head>

<body>
    <h1>抽選</h1>

    <!-- フォームの追加 -->
    <form method="POST" action="/confirm">
        <table>
            <thead>
                <tr>
                    <th>賞品</th>
                    <th>ID</th>
                    <th>所属</th>
                    <th>氏名</th>
                </tr>
            </thead>
            <tbody>
                {% for winner in winners %}
                <tr>
                    <td>{{ winner.prize }}</td>
                    <td>{{ winner.id }}</td>
                    <td>{{ winner.comp }}</td>
                    <td>{{ winner.name }}</td>
                    <td>
                        <input type="hidden" name="prize" value="{{ winner.prize }}">
                        <input type="hidden" name="id" value="{{ winner.id }}">
                        <input type="hidden" name="comp" value="{{ winner.comp }}">
                        <input type="hidden" name="name" value="{{ winner.name }}">
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>

        <!-- 確定ボタン -->
        <button type="submit" class="shuffle-link">確定</button>
    </form>

    <a href="/shuffle" class="shuffle-link">Shuffle</a>

    <!-- CSVダウンロードボタンの追加 -->
    <a href="/download-csv" class="shuffle-link">結果をダウンロード (CSV)</a>
</body>

</html>