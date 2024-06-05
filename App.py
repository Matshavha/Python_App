from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Classification Map</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                }
                .content {
                    padding: 20px;
                }
                .map-container {
                    width: 80%;
                    height: 500px;
                    margin: 0 auto;
                    border: 1px solid #ccc;
                }
                iframe {
                    width: 100%;
                    height: 100%;
                }
            </style>
        </head>
        <body>
            <div class="content">
                <h1>Classification Map</h1>
                <div class="map-container">
                    <iframe src="https://classify.azureedge.net/Feeders_Classification/Classification_Map.html" frameborder="0"></iframe>
                </div>
            </div>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
