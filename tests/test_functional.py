from flask_testing import LiveServerTestCase
import wsgi
from selenium import webdriver


class FunctionalTest(LiveServerTestCase):
    def create_app(self):
        app = wsgi.app
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        return app

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_root_title(self):
        # Showerbugs enter the root page
        self.browser.get(self.get_server_url())
        # Showerbugs can see "how was your day"
        self.assertEqual("How was your day", self.browser.title)