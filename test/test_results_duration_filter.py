import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage
from logic.results_page import ResultsPage


class TestResultDurationFilter(unittest.TestCase):
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

    def test_short_videos_filter(self):
        self.result_page.click_filter_button()
        time.sleep(2)
        self.result_page.click_Search_for_Under_4_minutes()
        time.sleep(2)
        results = self.result_page.get_first_5_results()
        result_times = [self.result_page.get_result_video_duration(self, result) for result in results]
        for t in result_times:
            self.assertGreaterEqual(self.config.get_value(self, "short_video_max"), t)

    def test_medium_videos_filter(self):
        self.result_page.click_filter_button()
        time.sleep(2)
        self.result_page.click_Search_for_4_to_20_minutes()
        time.sleep(2)
        results = self.result_page.get_first_5_results()
        result_times = [self.result_page.get_result_video_duration(self, result) for result in results]
        for t in result_times:
            self.assertGreaterEqual(self.config.get_value(self, "medium_video_max"), t)
            self.assertLessEqual(self.config.get_value(self, "short_video_max"), t)

    def test_long_videos_filter(self):
        self.result_page.click_filter_button()
        time.sleep(2)
        self.result_page.click_search_for_over_20_minutes()
        time.sleep(2)
        results = self.result_page.get_first_5_results()
        result_times = [self.result_page.get_result_video_duration(self, result) for result in results]
        for t in result_times:
            self.assertLessEqual(self.config.get_value(self, "medium_video_max"), t)


if __name__ == "__main__":
    unittest.main()
