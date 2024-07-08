import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage


class TestSwitchLanguage(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver("home_page")
        cls.home_page = HomePage(cls.driver)
        cls.config = ConfigProvider()

    @classmethod
    def tearDown(cls):
        cls.driver.close()

    def test_switch_to_hebrew(self):
        self.home_page.click_hebrew_language()
        time.sleep(2)
        self.assertEqual(self.home_page.get_first_use_title(),"כדאי להתחיל לחפש")

    def test_switch_to_english(self):
        self.home_page.click_english_language()
        time.sleep(2)
        self.assertEqual(self.home_page.get_first_use_title(), "Try searching to get started")


if __name__ == "__main__":
    unittest.main()
