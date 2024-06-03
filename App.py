from flask import Flask, render_template_string
from flask_compress import Compress

app = Flask(__name__)
Compress(app)

@app.route('/')
def map():
    return render_template_string('''
    <!doctype html>
    <html>
        <head>
            <title>Map</title>
        </head>
        <body>
            <iframe src="{{ url_for('static', filename='Voronoi_Map.html') }}" width="100%" height="600" loading="lazy"></iframe>
        </body>
    </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
