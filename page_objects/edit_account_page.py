from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class EditAccountPage(object):

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

        self.rhs = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#column-right')))

        self.first_name = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-firstname')))

        self.last_name = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-lastname')))

        self.email = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-email')))

        self.telephone = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-telephone')))

    def get_first_name(self):
        return self.first_name.get_attribute("value")

    def get_last_name(self):
        return self.last_name.get_attribute("value")

    def get_email(self):
        return self.email.get_attribute("value")

    def get_telephone(self):
        return self.telephone.get_attribute("value")
