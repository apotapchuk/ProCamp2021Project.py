import allure
import pytest
import requests
from config.readers import Config
from src.applications.api_clients.web_app_api_client import WebApiClient, PATH
from config.config import ConfigModel, get_config_variable_by_name
from config.webdriver_factory import get_webdriver
from config.settings import USERNAME1_INVALID, PASSWORD1_INVALID
from src.applications.api_client.web_app_api_client import WebApiClient

@pythest.fixture('session')
@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.positive
def pytest_addoption(parser):
    parser.adoption('--browser', 'store', None)
    parser.adoption('--browser', 'store', 'Chrome', 'Please choose a browser as a required parameter:--browser')

def browser(self, config):
    self.browser = config.get_config('BROWSER')
    if not browser:
        self.browser = request.config.getOption('--BROWSER')
        return browser

def driver(self):
    self.driver = get_webdriver(BROWSER)
    driver.implicitly_wait(10)
    driver.set_window_size[1020, 1080]
    yield driver

def get_new_user(self):
    self.user = new_user()
    self.new_username = UserFactory.get_user_username()
    self.new_password = UserFactory.get_new_user.passw()
    return new_user()

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.positive
@allure.story('User login to the site')
def test_get_new_user(new_user):
    step1 = runnerFactory.get('api', new_user.email, new_user.passw)
    assert step1(new_user) is True

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.positive
@pytest.mark.parametrize("BROWSERS", chrome, firefox, edge, opera)
@allure.story('Open LoginPage')
def test_open_login_page(self):
    self.get_url(self.BASE_URL + "/login")
    for i in range(50):
        elem = driver.find_element_by_class_name('cid4')
        elem.click()
        assert driver.find_element_by_class_name('mobile-nav-toggle')
    except requests.exceptions.HTTPErrorException

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.negative
@allure.story('User1 not login to the site')
def test_unsuccessful_login():
    self.get_url(self.BASE_URL + "/#/login")
    response = WebApiClient.login(USERNAME1_INVALID, PASSWORD1_INVALID)
    driver.find_element_by_id(email-helper-text, "Invalid email address")
    assert response['token'] is None
    assert not driver.find_element_by_id(email-helper-text, "Invalid email address")

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.positive
@pytest.mark.parametrize("BROWSERS", chrome, firefox, edge, opera)
@allure.story('User1 login to the site')
def test_login_to_the_site(new_user1):
    self.get_url(self.BASE_URL + "/#/login")
    wait(0.5)
    self.send_text(new_user1.USERNAME, By.ID, "email")
    self.send_text(new_user1.PASSWORD, By.ID, "password")
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
    step1 = UserFactory.login(new_user2.USERNAME, )
    assert step1.custom_assert() is True

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.negative
@pytest.mark.parametrize("BROWSERS", chrome, firefox, edge, opera)
@allure.story('Unsuccessful login to the site')
def test_unsuccessful_login():
    response = WebApiClient.login(USERNAME1_INVALID, PASSWORD1_INVALID)
    assert response['token'] is None
    assert response_status_code == 401

@pytest.mark.smoke
@pytest.mark.api
@pytest.mark.negative
@pytest.mark.parametrize("BROWSERS", chrome, firefox, edge, opera)
@allure.story('Unsuccessful login to the site')
def test_login_negative():
    r = requests.post(Config.BASE_URL+PATH.LOGIN_PATH)
    r.raise_for_status()
    assert r.json['token'] is None

