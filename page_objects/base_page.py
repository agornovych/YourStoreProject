from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage
from page_objects.registration_page import RegistrationPage


class BasePage(object):

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver
        try:
            self.web_driver.maximize_window()
        except WebDriverException:
            pass
        self.web_driver.get("http://localhost/")

        self.top_links = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#top-links')))

        self.my_account = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#top-links .dropdown .dropdown-toggle')))

        self.card_total = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#cart-total')))

    @property
    def register(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Register')]")))

    @property
    def login(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Login')]")))

    def go_to_registration(self):
        self.my_account.click()
        self.register.click()
        return RegistrationPage(self.web_driver)

    def go_to_login(self):
        self.my_account.click()
        self.login.click()
        return LoginPage(self.web_driver)