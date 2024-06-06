from flask import Flask, render_template, jsonify
import json
import gzip

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/geojson')
def geojson():
    with gzip.open('static/Classification_Map.geojson.gz', 'rt', encoding='utf-8') as f:
        geojson_data = json.load(f)
    return jsonify(geojson_data)

if __name__ == '__main__':
    app.run(debug=True)
