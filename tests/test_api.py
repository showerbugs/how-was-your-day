import unittest
import wsgi


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = wsgi.app.test_client()

    def test_root_page(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)
        self.assertIn("How was your day", response.data.decode())
