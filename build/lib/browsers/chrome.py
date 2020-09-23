from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from browsers.abstract_browser import AbstractBrowser


class Chrome(AbstractBrowser):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument('ignore-certificate-errors')
        super().__init__(name="Chrome",
                         webdriver_class=webdriver.Chrome,
                         webdriver_manager=ChromeDriverManager(),
                         desired_capabilities=DesiredCapabilities.CHROME.copy(),
                         chrome_options=chrome_options)

class ChromeRemote(AbstractBrowser):
    def __init__(self, command_executor):
        chrome_capabilities = DesiredCapabilities.CHROME.copy()
        chrome_capabilities["acceptSslCerts"] = True

        super(ChromeRemote, self).__init__(name="Chrome",
                                           command_executor=command_executor,
                                           desired_capabilities=chrome_capabilities)