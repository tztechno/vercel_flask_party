<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Screen Controller</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
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

        .grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
            width: 90%;
            max-width: 1000px;
        }

        .card {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 20px;
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
        }

        a {
            text-decoration: none;
            color: #34495e;
            font-weight: bold;
            transition: color 0.3s ease;
        }

        a:hover {
            color: #3498db;
        }

        @media (max-width: 768px) {
            .grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }

        @media (max-width: 480px) {
            .grid {
                grid-template-columns: 1fr;
            }

            h1 {
                font-size: 28px;
            }
        }
    </style>
</head>

<body>
    <h1>Screen Controller</h1>
    <div>
        <h2>現在のページ: <span id="currentPage">{{ current_page }}</span></h2>
    </div>
    <div class="grid">
        {% for page in selectable_pages %}
        <div class="card">
            <a href="javascript:void(0);" onclick="setPage('{{ page }}')">{{ page }}</a>
        </div>
        {% endfor %}
    </div>

    <div class="preview-section">
        <h2>プレビュー:</h2>
        <iframe id="previewFrame" src="{{ current_page }}"></iframe>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
        function setPage(page) {
            axios.post('/set_current_page', { page: page })
                .then(function (response) {
                    if (response.data.success) {
                        document.getElementById('currentPage').textContent = response.data.current_page;
                        document.getElementById('previewFrame').src = response.data.current_page;
                    } else {
                        alert('ページの変更に失敗しました');
                    }
                })
                .catch(function (error) {
                    console.error('Error:', error);
                    alert('エラーが発生しました');
                });
        }

        // 定期的に現在のページを更新
        setInterval(function () {
            axios.get('/get_current_page')
                .then(function (response) {
                    const currentPage = response.data.current_page;
                    document.getElementById('currentPage').textContent = currentPage;
                    document.getElementById('previewFrame').src = currentPage;
                })
                .catch(function (error) {
                    console.error('Error:', error);
                });
        }, 5000); // 5秒ごとに更新
    </script>
</body>

</html>