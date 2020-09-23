from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from random import randint

from page_objects.checkout_page import CheckoutPage


class CartPage(object):

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

        self.checkout_button = WebDriverWait(self.web_driver, 20). \
            until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Checkout')]")))

    def go_to_checkout(self):
        self.checkout_button.click()
        return CheckoutPage(self.web_driver)
