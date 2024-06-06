from flask import Flask, render_template, send_from_directory
import json
import gzip

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/geojson')
def geojson():
    return send_from_directory('static', 'data_Classification_Map.json.gz')

if __name__ == '__main__':
    app.run(debug=True)
