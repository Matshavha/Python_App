from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def map():
    # Use the URL from your Azure Storage
    map_url = "https://classificationmaps.blob.core.windows.net/feedersclassify/Classification_Map.html"
    return render_template_string(f"""
    <!doctype html>
    <html>
        <head>
            <title>Map</title>
        </head>
        <body>
            <iframe src="{map_url}" width="100%" height="600"></iframe>
        </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)

