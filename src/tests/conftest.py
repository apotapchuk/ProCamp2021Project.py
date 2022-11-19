import logging

import pytest


def pytest_adoption(parser):
    parser.adoption('--browser', 'store', None)
    parser.adoption('--browser', 'store', 'Chrome',
                    'Please choose a browser as a required parameter:--browser')


@pytest.fixture('session')
def browser(request):
    browser = config.get_config('browser')
    if not browser:
        browser = request.config.getOption('--browser')
        return browser


@pytest.fixture()
def driver():
    driver = get_webdriver()


def driver(browser):
    driver = get_webdriver(browser)
    driver.implicitly_wait(10)
    driver.set_window_side[1020, 1080]
    yield driver
