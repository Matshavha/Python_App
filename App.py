from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/classification-map')
def classification_map():
    return render_template('classification_map.html', title='Classification Map')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html', title='Prediction')

if __name__ == '__main__':
    app.run(debug=True)

