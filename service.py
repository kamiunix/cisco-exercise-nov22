from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///malicious_urls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['BASIC_AUTH_USERNAME'] = 'username'
app.config['BASIC_AUTH_PASSWORD'] = 'password'
db = SQLAlchemy(app)
basic_auth = BasicAuth(app)

# Define the MaliciousURL model with an explicit table name
class MaliciousURL(db.Model):
    __tablename__ = 'malicious_url'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), unique=True, nullable=False)

@app.route('/v1/urlinfo/<path:resource_url>', methods=['GET'])
@basic_auth.required
def check_url(resource_url):
    url_exists = MaliciousURL.query.filter_by(url=resource_url).first()
    if url_exists:
        return jsonify({'url': resource_url, 'safe': False, 'message': 'This URL is known to contain malware'}), 200
    else:
        return jsonify({'url': resource_url, 'safe': True, 'message': 'This URL is safe to access'}), 200

if __name__ == '__main__':
    app.run(debug=False)
