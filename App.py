from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Home</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                }
                nav ul {
                    list-style: none;
                    background-color: #333;
                    padding: 10px;
                    margin: 0;
                    text-align: center;
                }
                nav ul li {
                    display: inline;
                    margin-right: 10px;
                }
                nav ul li a {
                    color: white;
                    text-decoration: none;
                }
                .content {
                    padding: 20px;
                }
            </style>
        </head>
        <body>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/classification-map">Classification Map</a></li>
                    <li><a href="/prediction">Prediction</a></li>
                </ul>
            </nav>
            <div class="content">
                <h1>Welcome to the Home Page</h1>
                <p>This is the home page of our Flask web application.</p>
            </div>
        </body>
        </html>
    ''')

@app.route('/about')
def about():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>About</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                }
                nav ul {
                    list-style: none;
                    background-color: #333;
                    padding: 10px;
                    margin: 0;
                    text-align: center;
                }
                nav ul li {
                    display: inline;
                    margin-right: 10px;
                }
                nav ul li a {
                    color: white;
                    text-decoration: none;
                }
                .content {
                    padding: 20px;
                }
            </style>
        </head>
        <body>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/classification-map">Classification Map</a></li>
                    <li><a href="/prediction">Prediction</a></li>
                </ul>
            </nav>
            <div class="content">
                <h1>About Us</h1>
                <p>This is the about page.</p>
            </div>
        </body>
        </html>
    ''')

@app.route('/classification-map')
def classification_map():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Classification Map</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                }
                nav ul {
                    list-style: none;
                    background-color: #333;
                    padding: 10px;
                    margin: 0;
                    text-align: center;
                }
                nav ul li {
                    display: inline;
                    margin-right: 10px;
                }
                nav ul li a {
                    color: white;
                    text-decoration: none;
                }
                .content {
                    padding: 20px;
                }
                .map-container {
                    width: 80%;
                    height: 500px;
                    margin: 0 auto;
                    border: 1px solid #ccc;
                }
                iframe {
                    width: 100%;
                    height: 100%;
                }
            </style>
        </head>
        <body>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/classification-map">Classification Map</a></li>
                    <li><a href="/prediction">Prediction</a></li>
                </ul>
            </nav>
            <div class="content">
                <h1>Classification Map</h1>
                <div class="map-container">
                    <iframe src="https://classify.azureedge.net/Feeders_Classification/Classification_Map.html" frameborder="0"></iframe>
                </div>
            </div>
        </body>
        </html>
    ''')

@app.route('/prediction')
def prediction():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Prediction</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f4;
                }
                nav ul {
                    list-style: none;
                    background-color: #333;
                    padding: 10px;
                    margin: 0;
                    text-align: center;
                }
                nav ul li {
                    display: inline;
                    margin-right: 10px;
                }
                nav ul li a {
                    color: white;
                    text-decoration: none;
                }
                .content {
                    padding: 20px;
                }
            </style>
        </head>
        <body>
            <nav>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/classification-map">Classification Map</a></li>
                    <li><a href="/prediction">Prediction</a></li>
                </ul>
            </nav>
            <div class="content">
                <h1>Prediction</h1>
                <p>This is the prediction page.</p>
            </div>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)
