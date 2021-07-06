import allure

from api_client.method_api import ApiClient


class TestGetMainPage:
    def __init__(self):
        pass

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.api_check
    @pytest.mark.parametrize("BROWSERS", chrome, firefox, edge, opera)
    @allure.story('Get MainPage')
    def test_check_title(self, driver):
        self.mainpage = MainPage(driver)
        response = str(api_page.get(Configuration.BASE_URL))
        assertEqual(response.status_code, 200).self
        assert mainpage.is_block_title_present(), 'title is not present on mainpage'

    def pytest_addoption(parser):
        parser.adoption('--browser', 'store', None)
        parser.adoption('--browser', 'store', 'Chrome',
                        'Please choose a browser as a required parameter:--browser')
