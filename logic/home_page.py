from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from logic.base_page_app import BasePageApp


class HomePage(BasePageApp):

    def __init__(self, driver):
        super().__init__(driver)

    def get_first_use_title(self):
        try:
            title = self._driver.find_element(By.XPATH, '//yt-formatted-string[@id="title"]')
            return title.text
        except NoSuchElementException as e:
            print("NoSuchElementException", e)
