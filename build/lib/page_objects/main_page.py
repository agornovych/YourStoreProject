from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from page_objects.news_letter_signup_page import NewsLetterSignUpPage
from page_objects.home_page import HomePage
import time


class MainPage(object):

    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver
        try:
            self.web_driver.maximize_window()
        except WebDriverException:
            pass
        self.web_driver.get("https://pp2.emiratesholidays.com")

        self.country_selector = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'div.country-indicator-button')))

        self.emiratesholidays_logo = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#headerlogo")))

        self.signup_button = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.toolbar-menu .signup-button')))

        self.cookies = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[ng-click*=acceptCookies]')))
                                                                   # .accept-cookies-banner .button")))

    def accept_cookies(self):
        self.cookies.click()
        return self

    def select_domain(self, country, lang='English'):
        self.accept_cookies()
        self.country_selector.click()
        # Select region
        if country in ['USA', 'Rest of the world']:
            country = 'U.S.A.'
            americas = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.region-1')))
            americas.click()
        elif country in ['Germany', 'United Kingdom', 'Ireland', 'Sweden', 'Denmark']:
            europe = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.region-2')))
            europe.click()
        elif country in ['Saudi Arabia', 'Oman', 'Bahrain', 'United Arab Emirates', 'Kuwait', 'Lebanon', 'Jordan', 'Iran, Islamic Republic Of']:
            middle_east = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.region-3')))
            middle_east.click()
        elif country in ['Nigeria', 'South Africa', 'Kenya', 'Egypt', 'Ghana', 'Zambia']:
            africa = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.region-4')))
            africa.click()
        elif country in ['India']:
            asia = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.region-5')))
            asia.click()
        else:
            pass
        # Transform lang
        if lang=='Arabic':
            lang='العربية'
        if country == 'Germany':
            lang = 'Deutsch'
        elif country == 'Sweden':
            lang = 'Svenska'
        elif country == 'Denmark':
            lang = 'Dansk'
        # Select country and language
        Select(WebDriverWait(self.web_driver, 15). \
            until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='points-of-sale-nav-country-select-wrapper']//select"))))\
            .select_by_visible_text(country)
        Select(WebDriverWait(self.web_driver, 15). \
            until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='points-of-sale-nav-language-select-wrapper']//select"))))\
            .select_by_visible_text(lang)
        # Confirm button
        confirm_button=self.web_driver.find_element_by_css_selector('.points-of-sale-nav button')
        confirm_button.click()
        # Country picker
        contry_picker = self.web_driver.find_element_by_css_selector('.country-picker a')
        contry_picker.click()
        return HomePage(self.web_driver)

    def click_news_letter_signup(self):
        self.signup_button.click()
        return NewsLetterSignUpPage(self.web_driver)