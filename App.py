from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def map():
    # Replace the below URL with the URL of your map.html file in Azure Storage
    map_url = "https://classificationmap.blob.core.windows.net/feederclassify/Classification_Map.html"
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
