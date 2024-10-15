<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Confirm Winners - {{ current_prize }}</title>
</head>

<body>
    <h1>Confirm Winners - {{ current_prize }}</h1>

    <table>
        <thead>
            <tr>
                <th>Prize</th>
                <th>ID</th>
                <th>Company</th>
                <th>Name</th>
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

    <!-- ページナビゲーション -->
    <div>
        {% if page_num > 1 %}
        <a href="{{ url_for('confirm', page_num=page_num-1) }}">前のページ</a>
        {% endif %}

        {% if page_num < total_pages %} <a href="{{ url_for('confirm', page_num=page_num+1) }}">次のページ</a>
            {% endif %}
    </div>
</body>

</html>