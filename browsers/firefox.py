from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, FirefoxProfile
from webdriver_manager.firefox import GeckoDriverManager

from browsers.abstract_browser import AbstractBrowser


class Firefox(AbstractBrowser):
    def __init__(self):
        firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
        firefox_capabilities["acceptSslCerts"] = True
        super().__init__(name="Firefox",
                         webdriver_class=webdriver.Firefox,
                         webdriver_manager=GeckoDriverManager(),
                         desired_capabilities=firefox_capabilities,
                         firefox_profile=FirefoxProfile()
                         )


class FirefoxRemote(AbstractBrowser):
    def __init__(self, command_executor):
        firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
        firefox_capabilities["acceptSslCerts"] = True
        super().__init__(name="Firefox",
                         command_executor=command_executor,
                         desired_capabilities=firefox_capabilities,
                         firefox_profile=FirefoxProfile()
                         )