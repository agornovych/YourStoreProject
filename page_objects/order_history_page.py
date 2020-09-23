from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class OrderHistoryPage(object):

    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

        self.order_status = WebDriverWait(self.web_driver, 10). \
            until(expected_conditions.presence_of_element_located((By.XPATH, '//tbody//tr[1]//td[4]')))