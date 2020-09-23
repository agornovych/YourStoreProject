from selenium.webdriver import Remote, DesiredCapabilities
from webdriver_manager.manager import DriverManager
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.chrome.options import Options


class AbstractBrowser(object):
    def __init__(self,
                 name,
                 webdriver_class=None,
                 webdriver_manager: DriverManager = None,
                 desired_capabilities: DesiredCapabilities = None,
                 firefox_profile: FirefoxProfile = None,
                 chrome_options: Options = None,
                 command_executor=None
                 ):
        self.name = name
        self.chrome_options = chrome_options
        self.firefox_profile = firefox_profile
        self.command_executor = command_executor
        self.desired_capabilities = desired_capabilities
        self.webdriver_manager = webdriver_manager
        self.__web_driver = Remote(command_executor=command_executor,
                                   desired_capabilities=desired_capabilities,
                                   browser_profile=firefox_profile,
                                   keep_alive=True) if command_executor and not webdriver_manager \
            else self.get_webdriver(webdriver_class=webdriver_class,
                                    webdriver_manager=webdriver_manager,
                                    desired_capabilities=desired_capabilities,
                                    firefox_profile=firefox_profile,
                                    chrome_options=chrome_options)

    def get_webdriver(self,
                      webdriver_class,
                      webdriver_manager: DriverManager,
                      desired_capabilities: DesiredCapabilities = None,
                      firefox_profile: FirefoxProfile = None,
                      chrome_options: Options = None) -> Remote:
        call_options = {"executable_path": webdriver_manager.install()} if webdriver_manager else dict()
        if desired_capabilities:
            call_options["desired_capabilities"] = desired_capabilities

        if firefox_profile:
            call_options["firefox_profile"] = firefox_profile

        if chrome_options:
            call_options["options"] = chrome_options

        return webdriver_class(**call_options)

    @property
    def web_driver(self):
        return self.__web_driver
