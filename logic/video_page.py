import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from logic.base_page_app import BasePageApp
from infra.utils import convert_numberK_to_number, convert_ago_time


class VideoPage(BasePageApp):
    SORT_BY_DROPDOWN = '//yt-dropdown-menu[@icon-label="Sort by"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._sort_by_dropdown = self._driver.find_element(By.XPATH, self.SORT_BY_DROPDOWN)

    def click_sort_by_dropdown(self):
        self._sort_by_dropdown.click()
        time.sleep(2)  # wait for animation

    def click_sort_by_top_comments(self):
        self.click_sort_by_dropdown()
        try:
            top_comments = self._sort_by_dropdown.find_element(By.XPATH, '//div[contains(text(), "Top comments")]')
            top_comments.click()
        except NoSuchElementException as e:
            print(f"could not find sort-by top comments button: {e}")

    def click_sort_by_newest_first(self):
        self.click_sort_by_dropdown()
        try:
            top_comments = self._sort_by_dropdown.find_element(By.XPATH, '//div[contains(text(), "Newest first")]')
            top_comments.click()
        except NoSuchElementException as e:
            print(f"could not find sort-by newest first button: {e}")

    def get_first_5_comments(self):
        try:
            comments = self._driver.find_elements(By.XPATH, '//ytd-comment-thread-renderer[position()<=5]')
            return comments
        except NoSuchElementException as e:
            print(f"could not find first 5 comments: {e}")

    @staticmethod
    def get_comment_likes(self, comment):
        try:
            comment_likes = comment.find_element(By.XPATH, '//span[@id="vote-count-middle"]')
            return convert_numberK_to_number(comment_likes.text)
        except NoSuchElementException as e:
            print(f"could not find comment likes: {e}")

    @staticmethod
    def get_comment_timestamp(self, comment):
        try:
            comment_time = comment.find_element(By.XPATH, '//span[@id="published-time-text"]')
            return convert_ago_time(comment_time.text)
        except NoSuchElementException as e:
            print(f"could not find comment timestamp: {e}")
