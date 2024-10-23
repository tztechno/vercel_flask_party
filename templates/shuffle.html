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
            margin-bottom: 20px;
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

        .button {
            display: inline-block;
            padding: 10px 15px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            border: none;
            cursor: pointer;
            margin: 5px;
        }

        .button:hover {
            background-color: #45a049;
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
        // 既存のスクリプト部分は省略...

        function downloadCSV() {
            const table = document.querySelector('table');
            const rows = table.querySelectorAll('tr');

            let csvContent = '\uFEFF'; // BOMを追加

            // ヘッダー行
            const headers = ["prize_id", "id", "comp", "name"];
            csvContent += headers.map(header => `"${header}"`).join(',') + '\n';

            // データ行
            rows.forEach((row, index) => {
                if (index === 0) return; // ヘッダー行をスキップ

                const cells = row.querySelectorAll('td');
                if (cells.length >= 4) { // hidden inputsの列を除外
                    const rowData = [
                        cells[0].textContent, // prize_id
                        cells[1].textContent, // id
                        cells[2].textContent, // comp
                        cells[3].textContent  // name
                    ].map(content => `"${content.trim()}"`);

                    csvContent += rowData.join(',') + '\n';
                }
            });

            // CSVファイルとしてダウンロード
            const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8' });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = 'winners.csv';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            URL.revokeObjectURL(link.href);
        }
    </script>
</head>

<body>
    <h1>抽選</h1>

    <!-- フォームの追加 -->
    <form method="POST" action="/confirm">
        <table>
            <thead>
                <tr>
                    <th>賞品ID</th>
                    <th>ID</th>
                    <th>所属</th>
                    <th>氏名</th>
                </tr>
            </thead>
            <tbody>
                {% for winner in winners %}
                <tr>
                    <td>{{ winner.prize_id }}</td>
                    <td>{{ winner.id }}</td>
                    <td>{{ winner.comp }}</td>
                    <td>{{ winner.name }}</td>
                    <td>
                        <input type="hidden" name="prize_id" value="{{ winner.prize_id }}">
                        <input type="hidden" name="id" value="{{ winner.id }}">
                        <input type="hidden" name="comp" value="{{ winner.comp }}">
                        <input type="hidden" name="name" value="{{ winner.name }}">
                    </td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </form>

    <!-- ボタン群 -->
    <div class="button-container">
        <form action="/shuffle" method="get" style="display: inline;">
            <button type="submit" class="button">Shuffle</button>
        </form>
        <button onclick="downloadCSV()" class="button">結果をダウンロード</button>
    </div>

</body>

</html>