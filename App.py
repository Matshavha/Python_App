from flask import Flask, render_template
import requests
import gzip
import io

app = Flask(__name__)

@app.route('/')
def home():
    # Fetch the compressed HTML map from the CDN
    url = 'https://classify.azureedge.net/Feeders_Classification/Classification_Map.html.gz'
    response = requests.get(url)

    # Decompress the HTML content
    compressed_content = io.BytesIO(response.content)
    with gzip.GzipFile(fileobj=compressed_content, mode='rb') as f:
        html_content = f.read().decode('utf-8')
    
    return render_template('index.html', map_content=html_content)

if __name__ == '__main__':
    app.run(debug=True)

