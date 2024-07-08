import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from logic.base_page_app import BasePageApp
from infra.utils import convert_numberK_to_number, convert_ago_time


class ResultsPage(BasePageApp):
    FILTER_BUTTON = '//div[@id="filter-button"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._filter_button = self._driver.find_element(By.XPATH, self.FILTER_BUTTON)

    def click_filter_button(self):
        self._filter_button.click()

    def click_Search_for_Under_4_minutes(self):
        try:
            self._driver.find_element(By.XPATH, '//div[@title="Search for Under 4 minutes"]').click()
        except NoSuchElementException as e:
            print(f"NoSuchElementException: {e}")

    def click_Search_for_4_to_20_minutes(self):
        try:
            self._driver.find_element(By.XPATH, '//div[@title="Search for 4 - 20 minutes"]').click()
        except NoSuchElementException as e:
            print(f"NoSuchElementException: {e}")

    def click_search_for_over_20_minutes(self):
        try:
            self._driver.find_element(By.XPATH, '//div[@title="Search for Over 20 minutes"]').click()
        except NoSuchElementException as e:
            print(f"NoSuchElementException: {e}")

    def get_first_5_results(self):
        try:
            results = self._driver.find_elements(By.XPATH, './/ytd-video-renderer')
            return results
        except NoSuchElementException as e:
            print(f"could not find first 5 results: {e}")

    @staticmethod
    def get_result_title(self, result):
        try:
            result_title = result.find_element(By.XPATH, '//a[@id="video-title"]')
            return result_title.get_attribute('title')
        except NoSuchElementException as e:
            print(f"could not find result title: {e}")

    @staticmethod
    def get_result_video_duration(self, result):
        try:
            result_time = result.find_element(By.XPATH, '//a[@id="video-title"]').get_attribute('aria-label')
            time_pattern = re.compile(r'(\d+)\s+minutes,\s+(\d+)\s+seconds')
            time_loooong = re.compile(r'(\d+)\s+hour')
            if time_loooong.search(result_time):
                return 21 * 60
            else:
                find_time = time_pattern.search(result_time)
                return int(find_time.group(1)) * 60 + int(find_time.group(2))

        except NoSuchElementException as e:
            print(f"NoSuchElementException: {e}")
