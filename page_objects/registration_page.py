from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from page_objects.account_page import AccountPage


class RegistrationPage(object):

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

        self.first_name = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-firstname')))

        self.last_name = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-lastname')))

        self.email = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-email')))

        self.telephone = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-telephone')))

        self.password = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-password')))

        self.confirm_password = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-confirm')))

        self.privacy_policy = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="agree"]')))

        self.submit_button = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]')))

    def enter_name(self, name):
        self.first_name.send_keys(name)
        return self

    def enter_last_name(self, last_name):
        self.last_name.send_keys(last_name)
        return self

    def enter_email(self, email):
        self.email.send_keys(email)
        return self

    def enter_telephone(self, telephone):
        self.telephone.send_keys(telephone)
        return self

    def enter_password(self, password):
        self.password.send_keys(password)
        return self

    def enter_confirm_password(self, password):
        self.confirm_password.send_keys(password)
        return self

    def tick_privacy_policy(self):
        self.privacy_policy.click()
        return self

    def click_submit(self):
        self.submit_button.click()
        return AccountPage(self.web_driver)