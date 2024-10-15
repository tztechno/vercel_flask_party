<!DOCTYPE html>
<html lang="ja">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Select Screen</title>
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
            margin-bottom: 20px;
            color: #2c3e50;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            /* カードの列数を4に変更 */
            gap: 10px;
            /* ギャップを小さく */
            width: 90%;
            max-width: 1000px;
        }

        .card {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 10px;
            /* パディングを小さく */
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 16px;
            /* フォントサイズを小さく */
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

        .preview-section {
            width: 100%;
            max-width: 1200px;
            margin-top: 30px;
        }

        #previewFrame {
            width: 100%;
            height: 600px;
            border: none;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
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

            .card {
                font-size: 14px;
                /* スマホ用にフォントサイズをさらに小さく */
            }
        }
    </style>
</head>

<body>
<body>
    <h1>Screen</h1>

    <div class="grid">
        {% for page in selectable_pages %}
        <div class="card">
            <button onclick="setPage('{{ page }}')">{{ nickname_map[page] }}</button>
        </div>
        {% endfor %}
    </div>

    <div class="preview-section">
        <iframe id="previewFrame" src="{{ current_page }}"></iframe>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
    <script>
        function setPage(page) {
            console.log('Selected page:', page);  // デバッグ用
            axios.post('/set_current_page', { page: page })
                .then(function (response) {
                    if (response.data.success) {
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
    </script>
</body>

</body>

</html>