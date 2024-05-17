from service import app, db, MaliciousURL
import json

def init_db():
    with open('malicious_urls.json', 'r') as f:
        malicious_urls = json.load(f)['urls']
        for url in malicious_urls:
            if not MaliciousURL.query.filter_by(url=url).first():
                db_url = MaliciousURL(url=url)
                db.session.add(db_url)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        init_db()
