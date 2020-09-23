from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from page_objects.order_history_page import OrderHistoryPage


class CheckoutPage(object):

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

        self.billing_continue_button = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#button-payment-address')))

    @property
    def first_name(self):
        return self.web_driver.find_element_by_css_selector('#input-payment-firstname')

    @property
    def last_name(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-payment-lastname')))

    @property
    def address_1(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-payment-address-1')))

    @property
    def city(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-payment-city')))

    @property
    def postcode(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-payment-postcode')))

    @property
    def country(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-payment-country')))

    @property
    def region_state(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#input-payment-zone')))

    @property
    def payment_existing_block(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#payment-existing')))

    @property
    def shipping_address_button(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#button-shipping-address')))

    @property
    def shipping_method_button(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#button-shipping-method')))

    @property
    def t_and_c_checkbox(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '[name=agree]')))

    @property
    def payment_method_button(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#button-payment-method')))

    @property
    def confirm_button(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, '#button-confirm')))

    @property
    def order_placed_message(self):
        return WebDriverWait(self.web_driver, 15). \
            until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'div#content h1')))
    # 'Your order has been placed!'

    @property
    def order_history_link(self):
        return WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#content [href*=order]')))

    def new_address(self):
        if self.payment_existing_block:
            self.web_driver.find_element_by_css_selector('input[value="new"]').click()
        else:
            pass

    def enter_name(self, name):
        self.first_name.send_keys(name)
        return self

    def enter_last_name(self, last_name):
        self.last_name.send_keys(last_name)
        return self

    def enter_address_1(self, address_1):
        self.address_1.send_keys(address_1)
        return self

    def enter_city(self, city):
        self.city.send_keys(city)
        return self

    def enter_postcode(self, postcode):
        self.postcode.send_keys(postcode)
        return self

    def select_country(self):
        Select(self.country).select_by_index(3)
        return self

    def select_region_state(self):
        Select(self.region_state).select_by_index(3)
        return self

    def press_billing_continue_button(self):
        self.billing_continue_button.click()
        return self

    def press_shipping_address_button(self):
        self.shipping_address_button.click()
        return self

    def press_shipping_method_button(self):
        self.shipping_method_button.click()
        return self

    def press_billing_continue(self):
        self.billing_continue_button.click()
        return self

    def tick_t_and_c_checkbox(self):
        self.t_and_c_checkbox.click()
        return self

    def press_payment_method_button(self):
        self.payment_method_button.click()
        return self

    def press_confirm_button(self):
        self.confirm_button.click()
        return self

    def go_to_order_history(self):
        self.order_history_link.click()
        return OrderHistoryPage(self.web_driver)