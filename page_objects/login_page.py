from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from page_objects.account_page import AccountPage


class LoginPage(object):

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

        self.email_address = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-email')))

        self.password = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-password')))

        self.submit_button = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '.well input[type="submit"]')))

    def enter_email(self, email):
        self.email_address.send_keys(email)
        return self

    def enter_password(self, password):
        self.password.send_keys(password)
        return self

    def click_login(self):
        self.submit_button.click()
        return self

    def do_login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        return AccountPage(self.web_driver)