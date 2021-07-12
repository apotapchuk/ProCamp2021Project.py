from selenium.webdriver.common.by import By
from config.config import Configurator
from cosmosid_pages.base_page import BasePage
from html.parser import HTMLParser


class MainPageLocations:
    BLOCK_TITLE = By.XPATH,'//h1[text()="Need Metagenomics Analysis?"]'


class MainPage(BasePage):
    def is_block_title_present(self):
        self.open_url(Configurator.BASE_URL)
        is_title = self.is_element_present(*MainPageLocators.BLOCK_TITLE)

        return is_title
