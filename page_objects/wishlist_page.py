from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class WishlistPage(object):

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

    @property
    def remove_button(self):
        return WebDriverWait(self.web_driver, 20). \
            until(expected_conditions.element_to_be_clickable(
            (By.CSS_SELECTOR, 'tbody [data-original-title="Remove"]')))

    @property
    def remove_message(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, '#account-wishlist [class="alert alert-success alert-dismissible"]')))

    def remove_item(self):
        self.remove_button.click()
        return self

    """Success: You have modified your wish list!"""
