from enum import Enum

from browsers import firefox, chrome, edge, ie, safari, android, ios


class Browsers(Enum):
    Firefox = (firefox.Firefox)
    FirefoxRemote = (firefox.FirefoxRemote)
    Chrome = (chrome.Chrome)
    ChromeRemote = (chrome.ChromeRemote)
    Edge = (edge.Edge)
    EdgeRemote = (edge.EdgeRemote)
    Ie = (ie.Ie)
    IeRemote = (ie.IeRemote)
    Safari = (safari.Safari)
    SafariRemote = (safari.SafriRemote)
    AndroidChrome = (android.Chrome)
    IOSSafari = (ios.Safari)

    def __init__(self, browser_class):
        self.browser_class = browser_class

    def __call__(self, *args, **kwargs):
        return self.browser_class(*args, **kwargs)