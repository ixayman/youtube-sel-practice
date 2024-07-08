import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils import check_if_array_in_descending_order
from logic.video_page import VideoPage


class TestDeviceTheme(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = BrowserWrapper()
        cls.driver = cls.browser.get_driver("adele-hello")
        cls.config = ConfigProvider()
        cls.driver.execute_script("window.scrollTo(0, 600)")
        time.sleep(2)
        cls.video_page = VideoPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_sort_comments_by_news_first(self):
        self.video_page.click_sort_by_newest_first()
        comments = self.video_page.get_first_5_comments()
        comment_timestamps = [self.video_page.get_comment_timestamp(self, comment) for comment in comments]
        self.assertTrue(check_if_array_in_descending_order(comment_timestamps))
        time.sleep(2)

    def test_sort_comments_by_top_comments(self):
        self.video_page.click_sort_by_top_comments()
        time.sleep(2)
        comments = self.video_page.get_first_5_comments()
        comment_likes = [self.video_page.get_comment_likes(self, comment) for comment in comments]
        for likes in comment_likes:
            self.assertGreaterEqual(likes, self.config.get_value(self, "adele-hello-minimum-likes"))



if __name__ == "__main__":
    unittest.main()