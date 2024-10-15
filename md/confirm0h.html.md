<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prize List</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f0f4f8;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            color: #333;
        }

        h1 {
            font-size: 36px;
            margin-bottom: 30px;
            color: #2c3e50;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        h2 {
            font-size: 28px;
            margin-bottom: 20px;
            color: #34495e;
        }

        table {
            width: 80%;
            max-width: 800px;
            border-collapse: separate;
            border-spacing: 0;
            background-color: white;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
            border-radius: 12px;
            overflow: hidden;
        }

        th,
        td {
            padding: 18px 24px;
            text-align: left;
        }

        th {
            background-color: #34495e;
            color: white;
            font-weight: 600;
            font-size: 18px;
            text-transform: uppercase;
        }

        td {
            font-size: 16px;
            border-bottom: 1px solid #ecf0f1;
        }

        tbody tr:last-child td {
            border-bottom: none;
        }

        tbody tr:hover {
            background-color: #f8f9fa;
            transition: background-color 0.3s ease;
        }

        @media (max-width: 600px) {
            table {
                width: 95%;
            }

            th,
            td {
                padding: 12px 16px;
            }

            h1 {
                font-size: 28px;
            }
        }
    </style>
</head>

<body>
    <h1>{{ winners[0].prize }}</h1> <!-- 当選者の賞品名を表示 -->
    <h2>当選者発表</h2>
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
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <div class="pagination">
        {% if page_num > 1 %}
        <a href="{{ url_for('confirm', page_num=page_num-1) }}">前へ</a>
        {% endif %}
        {% if page_num < total_pages %} <a href="{{ url_for('confirm', page_num=page_num+1) }}">次へ</a>
            {% endif %}
    </div>
</body>

</html>