from enum import Enum

from browsers import firefox, chrome


class Browsers(Enum):
    Firefox = firefox.Firefox
    Chrome = chrome.Chrome

    def __init__(self, browser_class):
        self.browser_class = browser_class

    def __call__(self, *args, **kwargs):
        return self.browser_class(*args, **kwargs)