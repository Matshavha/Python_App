from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def map():
    # Use the URL from your Azure Front Door
    map_url = "https://network-a2b8aec3h5hqduh0.z02.azurefd.net/feedersclassify/Classification_Map.html"
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
