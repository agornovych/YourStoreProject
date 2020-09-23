from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from page_objects.edit_account_page import EditAccountPage
from page_objects.home_page import HomePage


class AccountPage(object):

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

        self.rhs = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#column-right')))

    @property
    def logout_button(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.
                  element_to_be_clickable((By.XPATH, "//aside[@id='column-right']//a[contains(text(), 'Logout')]")))

    @property
    def login_button(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.
                  element_to_be_clickable((By.XPATH, "//aside[@id='column-right']//a[contains(text(), 'Login')]")))

    @property
    def edit_account(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.
                  element_to_be_clickable((By.CSS_SELECTOR, '#content [href*=edit]')))

    @property
    def home_button(self):
        return WebDriverWait(self.web_driver, 20). \
            until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Your Store')]")))

    def logout(self):
        self.logout_button.click()
        return self

    def go_to_edit_account(self):
        self.edit_account.click()
        return EditAccountPage(self.web_driver)

    def go_to_home_page(self):
        self.home_button.click()
        return HomePage(self.web_driver)

