from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from random import  randint

from page_objects.cart_page import CartPage
from page_objects.wishlist_page import WishlistPage


class HomePage(object):

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

        self.add_to_basket_buttons = WebDriverWait(self.web_driver, 20). \
            until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, '.row button[onclick*="cart.add"]')))

        self.add_to_wishlist_buttons = WebDriverWait(self.web_driver, 20). \
            until(expected_conditions.visibility_of_all_elements_located((By.CSS_SELECTOR, '.row button[onclick*="wishlist.add"]')))

        self.product_names = WebDriverWait(self.web_driver, 20). \
            until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, '.caption a')))

    @property
    def shopping_cart(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.
                  element_to_be_clickable((By.CSS_SELECTOR, '#top [title="Shopping Cart"]')))

    @property
    def wishlist(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.
                  element_to_be_clickable((By.CSS_SELECTOR, '#top [title*="Wish List"]')))

    @property
    def success_message(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.alert')))

    def add_product_to_basket(self):
        self.add_to_basket_buttons[1].click()
        return self

    def add_product_to_wishlist(self):
        self.add_to_wishlist_buttons[1].click()
        return self

    def get_product_name(self):
        for i in self.product_names:
            yield i

    def go_to_cart(self):
        self.shopping_cart.click()
        return CartPage(self.web_driver)

    def go_wishlist(self):
        self.wishlist.click()
        return WishlistPage(self.web_driver)