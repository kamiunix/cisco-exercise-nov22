from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load malicious URLs from JSON file / DB
with open('malicious_urls.json', 'r') as f:
    MALICIOUS_URLS = json.load(f)['urls']

@app.route('/v1/urlinfo/<path:resource_url>', methods=['GET'])
def check_url(resource_url):
    if resource_url in MALICIOUS_URLS:
        return jsonify({'url': resource_url, 'safe': False, 'message': 'This URL is known to contain malware'}), 200
    else:
        return jsonify({'url': resource_url, 'safe': True, 'message': 'This URL is safe to access'}), 200

if __name__ == '__main__':
    app.run(debug=True)

