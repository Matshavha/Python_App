from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def display_map():
    response = make_response(render_template('map.html'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
