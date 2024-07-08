from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class BasePageApp(BasePage):
    HOME_BUTTON = '//div[@id="masthead-container"]//a[@id="logo"]'
    SEARCH_FIELD = '//input[@id="search"]'
    SETTINGS_DROPDOWN_BUTTON = '//div[@id="masthead-container"]//button[@aria-label="Settings"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._home_button = self._driver.find_element(By.XPATH, self.HOME_BUTTON)
        self._search_field = self._driver.find_element(By.XPATH, self.SEARCH_FIELD)
        self._settings_dropdown_button = self._driver.find_element(By.XPATH, self.SETTINGS_DROPDOWN_BUTTON)

    def click_home_button(self):
        self._home_button.click()

    def click_settings_dropdown_button(self):
        self._settings_dropdown_button.click()

    def insert_in_search_field(self, value):
        self._search_field.click()
        self._search_field.clear()
        self._search_field.send_keys(value)

    def search_field_enter(self):
        self._search_field.send_keys(Keys.RETURN)

    def click_theme_menu(self):
        self._settings_dropdown_button.click()
        try:
            appearance = self._driver.find_element(By.XPATH, '//ytd-toggle-theme-compact-link-renderer')
            appearance.click()
        except NoSuchElementException as e:
            print("NoSuchElementException", e)

    def click_light_theme(self):
        self.click_theme_menu()
        try:
            light_theme = self._driver.find_element(By.XPATH, '//yt-formatted-string[contains(text(), "Light theme")]')
            light_theme.click()
        except NoSuchElementException as e:
            print("NoSuchElementException", e)

    def click_dark_theme(self):
        self.click_theme_menu()
        try:
            dark_theme = self._driver.find_element(By.XPATH, '//yt-formatted-string[contains(text(), "Dark theme")]')
            dark_theme.click()
        except NoSuchElementException as e:
            print("NoSuchElementException", e)

    def get_theme_flag(self):
        try:
            self._driver.find_element(By.XPATH, '//html[@dark]')
            return "dark theme"
        except NoSuchElementException as e:
            return "light theme"

    def click_language_menu(self):
        self._settings_dropdown_button.click()
        try:
            language = self._driver.find_element(By.XPATH, '//yt-formatted-string[contains(text(), "Language:")]')
            language.click()
        except NoSuchElementException as e:
            print("NoSuchElementException", e)

    def click_english_language(self):
        self.click_language_menu()
        try:
            english = self._driver.find_element(By.XPATH, '//yt-formatted-string[contains(text(), "English (US)")]')
            english.click()
        except NoSuchElementException as e:
            print("NoSuchElementException", e)

    def click_hebrew_language(self):
        self.click_language_menu()
        try:
            english = self._driver.find_element(By.XPATH, '//yt-formatted-string[contains(text(), "עברית")]')
            english.click()
        except NoSuchElementException as e:
            print("NoSuchElementException", e)
