from selenium.common.exceptions import NoSuchElementException
from html.parser import HTMLParser
from config.config import Pages
from config.settings import SITE_NAME, BASE_URL
from urllib.request import urlopen

class BasePage:
    def __init__(self, cosmosid, *args, **kwargs):
        self.links = BASE_URL
        self.site_name = Metagenomics Cloud
        super().__init__(*args, **kwargs)
        self.feed(self.read_site_content())
        self.write_to_file()
        self.driver = driver
        self.driver.get(BASE_PAGE)

    def open_url(self, BASE_URL):
        self.driver.get(BASE_URL)

    def find_element(self, *locator) -> list:
        return self.driver.find_element(*locator)

    def is_element_present(self, *locator):
        try:
            self.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    if not self.validate(attr[0]):
                        self.links.append(attr[1])

    def validate(self, link):
        return link in self.links or '#' in link or 'javascript:' in link

    def read_site_content(self):
        return str(urlopen(self.BASE_URL).read())


