from selenium.common.exceptions import NoSuchElementException
from config.config import Pages

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(BASE_PAGE)

    def open_url(self, URL):
        self.driver.get(URL)

    def find_element(self, *locator) -> list:
        return self.driver.find_element(*locator)

    def is_element_present(self, *locator):
        try:
            self.find_element(*locator)
        except NoSuchElementException:
            return False
        return True
