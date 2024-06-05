from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/call_url', methods=['GET'])
def call_url():
    # The URL to call, you can replace this with your target URL
    url = 'https://classify.azureedge.net/Feeders_Classification/Classification_Map.html'
    
    # Make a GET request to the specified URL
    response = requests.get(url)
    
    # Return the response content and status code
    return jsonify({
        'status_code': response.status_code,
        'content': response.text
    })

if __name__ == '__main__':
    app.run(debug=True)

