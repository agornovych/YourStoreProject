import pytest
import yaml
# from selenium.webdriver import DesiredCapabilities

from browsers.browsers import Browsers
from page_objects.base_page import BasePage


class Config(object):
    webdrivers = {}
    browsers = []
    grid_address = None
    current_browser = None
    brw = None


def pytest_addoption(parser):
    parser.addoption("--conf",
                     action='store',
                     help="Path to the environment configuration")


@pytest.fixture(scope='session', autouse=True)
def init_drivers(request):
    config = None
    with open(request.config.getoption("--conf")) as yaml_file:
        config = yaml.load(yaml_file)

    Config.browsers = config["browsers"]
    Config.grid_address = config["grid_url"]

    def _get_browser(browser_name):
        Config.webdrivers[browser_name] = Browsers[browser_name]

    for br in Config.browsers:
        _get_browser(br)


def get_browser():
    for i in Config.webdrivers:
        yield i


def get_base_page(browser):
    print(f"Browser: {Config.webdrivers[browser].name}")
    webdriver = Config.webdrivers[browser](command_executor=Config.grid_address) if "Remote" in Config.webdrivers[
        browser].name else Config.webdrivers[browser]()
    return BasePage(webdriver.web_driver)


@pytest.fixture
def base_page(request):
    next_brw = None
    if not Config.brw:
        Config.brw = get_browser()

    try:
        next_brw = Config.brw.__next__()
    except StopIteration:
        Config.brw = get_browser()
        next_brw = Config.brw.__next__()

    res = get_base_page(next_brw)

    def fin():
        res.web_driver.quit()

    request.addfinalizer(fin)

    return res


def pytest_generate_tests(metafunc):
    config = None
    with open(metafunc.config.getoption("--conf")) as yaml_file:
        config = yaml.load(yaml_file)
    params = tuple(map(lambda browser: (config["login"],
                                        config["password"]
                                        ),
                       config["browsers"]
                       )
                   )

    metafunc.parametrize("login, password", params)
