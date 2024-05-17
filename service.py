from flask_basicauth import BasicAuth
from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load malicious URLs from JSON file
with open('malicious_urls.json', 'r') as f:
    MALICIOUS_URLS = json.load(f)['urls']

# Configure basic authentication
app.config['BASIC_AUTH_USERNAME'] = 'username'
app.config['BASIC_AUTH_PASSWORD'] = 'password'
basic_auth = BasicAuth(app)

@app.route('/v1/urlinfo/<path:resource_url>', methods=['GET'])
@basic_auth.required
def check_url(resource_url):
    if resource_url in MALICIOUS_URLS:
        return jsonify({'url': resource_url, 'safe': False, 'message': 'This URL is known to contain malware'}), 200
    else:
        return jsonify({'url': resource_url, 'safe': True, 'message': 'This URL is safe to access'}), 200

if __name__ == '__main__':
    app.run(debug=False)

