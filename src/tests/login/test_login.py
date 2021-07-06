import logging
import allure
import pytest
import requests
from config.readers import Config
from src.applications.api_clients.web_app_api_client import WebApiClient, PATH
from config.config import configuration as config
from config.config import ConfigModel, get_config_variable_by_name
from config.webdriver_factory import get_webdriver
from allure import assert_that
from libs.api_client import ApiClient


class TestLoginPage:

    @pythest.fixture('session')
    def pytest_addoption(parser):
        parser.adoption('--browser', 'store', None)
        parser.adoption('--browser', 'store', 'Chrome', 'Please choose a browser as a required parameter:--browser')

    def browser(self, config):
        self.browser = config.get_config('browser')
        if not browser:
            self.browser = request.config.getOption('--browser')
            return browser

    def driver(self):
        self.driver = get_webdriver(browser)
        driver.implicitly_wait(10)
        driver.set_window_size[1020, 1080]
        yield driver

    def get_new_user(self):
        self.user = new_user()
        UserFactory.get_user(new_user)
        return new_user()

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.positive
    @allure.story('User1 login to the site')
    def test_get_new_user(new_user):
        step1 = runnerFactory.get('api', new_user.email, new_user.password)
        assert step1(new_user) is True

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.negative
    @allure.story('User1 not login to the site')
    def test_unsuccessful_login():
        response = WebApiClient.login("sdkfjkdsjnf", "kdlkf")
        assert response['token'] is None

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.positive
    @pytest.mark.parametrize("BROWSERS", chrome, firefox, edge, opera)
    @allure.story('Open LoginPage')
    def test_open_login_page(self):
        self.get_url(self.BASE_URL + "/#/login")

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.positive
    @pytest.mark.parametrize("BROWSERS", chrome, firefox, edge, opera)
    @allure.story('User1 login to the site')
    def test_login_to_the_site(new_user1):
        self.open_login_page()
        time.sleep(0.5)
        self.send_text(user.USERNAME, By.ID, "email")
        self.send_text(user.PASSWORD, By.ID, "password")
        self.click(By.XPATH, '//*/button[@type="SignIn-button"]')
        response = WebApiClient.login(get_config_variable_by_name(ConfigModel.USER),
                                      get_config_variable_by_name(ConfigModel.PASSWORD))
        assert response['token'] is not None
        assert response_status_code == 200

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.positive
    @pytest.mark.parametrize("BROWSERS", chrome, firefox, edge, opera)
    @allure.story('User2 login to the site')
    def test_random_user_login_to_the_site(new_user2):
        step1 = UserFactory.get('api').login(new_user2.USERNAME, new_user2.PASSWORD)
        assert step1.custom_assert() is True

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.negative
    @pytest.mark.parametrize("BROWSERS", chrome, firefox, edge, opera)
    @allure.story('Unsuccessful login to the site')
    def test_unsuccessful_login():
        response = WebApiClient.login(USERNAME1_INVALID, PASSWORD1_INVALID)
        assert response['token'] is None

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.negative
    @pytest.mark.parametrize("BROWSERS", chrome, firefox, edge, opera)
    @allure.story('Unsuccessful login to the site')
    def test_login_negative():
        r = requests.post(Config.BASE_URL+PATH.LOGIN_PATH)
        r.raise_for_status()
        assert r.json['token'] is None

