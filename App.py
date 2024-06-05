from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/classification-map', methods=['GET', 'POST'])
def classification_map():
    if request.method == 'POST':
        area = request.form['area']
        # Define locations for areas in Gauteng, South Africa
        if area.lower() == 'johannesburg':
            location = [-26.2041, 28.0473]
        elif area.lower() == 'pretoria':
            location = [-25.7479, 28.2293]
        else:
            # Default location if the input doesn't match known areas
            location = [-26.2041, 28.0473]  # Johannesburg as default

        return render_template('map.html', location=location)
    
    return render_template('classification_map.html', title='Classification Map')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html', title='Prediction')

if __name__ == '__main__':
    app.run(debug=True)
