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
    'Please choose a browser as a required parameter:--browser')

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
def login_request(request):
    if request.method == 'POST':
        form = LOGIN_PAGE(request, request.POST)
        if form.is_valid():
            username = UserFactory.get_

            exept Exception:
            logging.errorException(f"Failed to login as user")
            @allure.attach(str(request.function.get.result),
                          web_driver.get_screenshot_as_png(),
                          "screenshot",
                          allure.attachmentType.PNG)
            )
