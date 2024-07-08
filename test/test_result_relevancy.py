import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage
from logic.results_page import ResultsPage


class TestResultRelevancy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver("home_page")
        cls.home_page = HomePage(cls.driver)
        cls.config = ConfigProvider()
        time.sleep(2)  # wait for page to load
        cls.home_page.insert_in_search_field(cls.config.get_value(cls, "search_query"))
        cls.home_page.search_field_enter()
        time.sleep(2)  # wait for page to load
        cls.driver.get(cls.driver.current_url)
        time.sleep(2)  # wait for page to load
        cls.result_page = ResultsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_result_relevancy(self):
        results = self.result_page.get_first_5_results()

        result_titles = [self.result_page.get_result_title(self, result) for result in results]
        self.assertTrue(any(self.config.get_value(self, "search_query") in s for s in result_titles))

if __name__ == '__main__':
    unittest.main()