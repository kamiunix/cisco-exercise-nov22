import unittest
from service import app

class TestMalwareURLLookup(unittest.TestCase):
    def setUp(self):
        # Set up Flask test client
        self.app = app.test_client()

    def test_malicious_url(self):
        # Test a known malicious URL
        url = "malicious.com"
        response = self.app.get(f'/v1/urlinfo/{url}',
            headers={'Authorization': 'Basic dXNlcm5hbWU6cGFzc3dvcmQ='})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['safe'], False)

    def test_unknown_url(self):
        # Test an unknown URL
        url = "unknown.com"
        response = self.app.get(f'/v1/urlinfo/{url}',
            headers={'Authorization': 'Basic dXNlcm5hbWU6cGFzc3dvcmQ='})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['safe'], True)
        self.assertEqual(data['message'], 'This URL is safe to access')

    def test_auth_success(self):
        # Test authentication with correct credentials
        response = self.app.get('/v1/urlinfo/example.com',
                                headers={'Authorization': 'Basic dXNlcm5hbWU6cGFzc3dvcmQ='})
        self.assertEqual(response.status_code, 200)

    def test_auth_failure(self):
        # Test authentication with incorrect credentials
        response = self.app.get('/v1/urlinfo/example.com',
                                headers={'Authorization': 'Basic invalid_credentials'})
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()
