import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.base_page_app import BasePageApp


class TestDeviceTheme(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver("home_page")
        cls.base_page_app = BasePageApp(cls.driver)
        cls.config = ConfigProvider()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_switch_to_dark_mode(self):
        self.base_page_app.click_dark_theme()
        self.assertEqual(self.base_page_app.get_theme_flag(), "dark theme")

    def test_switch_to_light_mode(self):
        self.base_page_app.click_light_theme()
        self.assertEqual(self.base_page_app.get_theme_flag(), "light theme")


if __name__ == '__main__':
    unittest.main()
