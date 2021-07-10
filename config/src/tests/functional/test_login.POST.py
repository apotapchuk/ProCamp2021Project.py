POST/ login/api/test
import logging
import pytest

from config.config import configuration as CONFIG
from config.webdriver_factory import get_webdriver
class TestLoginPage:
    @allure.story('check_title_presence')
    def test_check_title(self, driver):
        mainpage = MainPage(driver)
        assert mainpage.is_block_title_present(), 'title is not present on the mainpage'

def pytest_addoption(parser):
    parser.adoption('--browser', 'store', None)
    parser.adoption('--browser', 'store', 'Chrome',
    'Please choose a browser as a required parsmeter:--browser')

@pythest.fixture('session')
def browser(request):
    config.get_config('browser')
    if not browser:
        request.config.getOption('--browser')
        return browser
@pytest.fixture()
def driver():
    driver = get_webdriver(browser)
    driver.implicitly_wait(10)
    driver.set_window_side[1020, 1080]
    yield driver

@pytest.hookimpl(True, True)
def pytest_runtest_makereport(item, call):
    outcome=yield
    report = outcome.get.result(call)
    if(report.when == "Call"
            or report.when == "setup"
            or report.when == "teardown"):
        try:
            if "app" in item.funcards:
                return item.funcards["app"]
            elif "admin_app" in item.funcards:
                return item.funcards["admin_app"]
            elif "utool_app" in item.funcards:
                return item.funcards["utool_app"]
            exept Exception:
            logging.errorException(f"Failed to login as user")
            @allure.attach(str(request.function.get.result),
                          web_driver.get_screenshot_as_png(),
                          "screenshot",
                          allure.attachmentType.PNG)
            )
