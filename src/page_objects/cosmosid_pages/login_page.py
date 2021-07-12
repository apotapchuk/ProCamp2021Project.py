from selenium.webdriver.common.by import By
from config.config import Configurator
from cosmosid_pages.base_page import BasePage
from config.config import Pages
from config.settings import LOGIN_PAGE

class LoginPageLocations:
    BLOCK_TITLE = By.XPATH,'//h1[text()="Sign in"]'


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(DRIVER)

    def open_url(self, LOGIN_PAGE):
        self.driver.get(LOGIN_PAGE)

    def find_element_by_id(self, *locator):
        self.driver.find_element_by_id(*locator)
        elem.send_keys(USERNAME)

    def find_element_by_label(self, *locator):
        return self.driver.find_elementby_label(*locator)

    def is_element_present(self, *locator):
        try:
            self.find_element(*locator)
        except NoSuchElementException:
            return False
        return True


class MainPage(BasePage):
    def is_block_title_present(self):
        self.open_url(Configurator.BASE_URL)
        is_title = self.is_element_present(*MainPageLocators.BLOCK_TITLE)

        return is_title
