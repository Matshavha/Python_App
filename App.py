from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/classification-map')
def classification_map():
    return render_template('classification_map.html')

@app.route('/statistics')
def statistics():
    return render_template('statistics.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
