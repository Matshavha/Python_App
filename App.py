from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def map():
    # Use the direct URL from your Azure Storage blob
    map_url = "https://classificationmap.blob.core.windows.net/feederclassify/Classification_Map.html"
    return render_template_string(f"""
    <!doctype html>
    <html>
        <head>
            <title>Map</title>
            <style>
                body {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .map-container {{
                    width: 80%;
                    height: 80%;
                    border: 1px solid #ccc;
                }}
            </style>
        </head>
        <body>
            <div class="map-container">
                <iframe src="{map_url}" width="100%" height="100%"></iframe>
            </div>
        </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)
