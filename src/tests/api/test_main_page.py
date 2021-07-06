import allure
import pytest
import requests
from distlib import database
from pip import configuration

from config.settings import HEADERS, OK, HEADERS_INVALID_USER, HEADERS_INVALID_PASS, UN_AUTH, ROOT_FOLDER_LOCATION, \
    TOKEN_INVALID, FORBIDDEN, SPECIFIC_FOLDER_NAME, SPECIFIC_FOLDER_NUMBER_FILES, SPECIFIC_FOLDER_LOCATION, RUNS, \
    ANALYSIS, ARTIFACTS, BASE_URL, ROOT_FOLDER_NAME
from src.applications.api_clients.methods import ApiClient


with requests.get(BASE_URL) as r:
    if r.status_code == 200:
        print(r.text)


class TestMainPageGet:

    @pytest.fixture(True, "session")
    @pytest.mark.api
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.request('GetMainPage')
    def test_get_mainpage(self):
        api_page = ApiClient()
        response = str(api_page.get(configuration.BASE_URL))
        assert '200' in response, f'Actual_status_code:{response}\nExpected: 200'

    def new_user(user_id, valueError=None):
        print("before new_user")
        database.connect()
        user = database.select(user_id, 'sergii.butenko@globallogic.com')
        if user is not None:
            raise valueError("No user in db")
        yield user
        print("after new_user")


class TestApi:
    api = ApiClient()

    @pytest.fixture(True, "function")
    @pytest.mark.api
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story('Successful login')
    def test_valid_login(self):
        with allure.step('Login to the site with valid credentials'):
            self.api.post_login(HEADERS, OK)

    @pytest.mark.api
    @pytest.mark.regression
    @pytest.mark.negative
    @allure.story('Login with invalid username')
    def test_login_invalid_username(self, IN_AUTH=None):
        with allure.step('Login  to the site with invalid username'):
            self.api.post_login(HEADERS_INVALID_USER, IN_AUTH)

    @pytest.mark.api
    @pytest.mark.regression
    @pytest.mark.negative
    @allure.story('Login with invalid password')
    def test_login_invalid_password(self, IN_AUTH=None):
        with allure.step('Login to the site with invalid password'):
            self.api.post_login(HEADERS_INVALID_PASS, IN_AUTH)

    @pytest.mark.api
    @pytest.mark.regression
    @pytest.mark.negative
    @allure.story('Login with invalid username and invalid password')
    def test_login_invalid_username_and_invalid_password(self):
        with allure.step('Login to the site with invalid username and invalid password'):
            self.api.post_login(HEADERS_INVALID_PASS, UN_AUTH)

    @pytest.mark.api
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story('Get files number from root folder')
    def test_get_files_number_from_root_folder(self, token, ROOT_FOLDER_NUMBER_FILES=None):
        with allure.step('Get files number from root folder'):
            folder_name, files_number = self.api.get_files_number(ROOT_FOLDER_LOCATION, token)
            assert folder_name == ROOT_FOLDER_NAME and files_number == ROOT_ROLDER_NUMBER_FILES,\
                f'Actual root folder name: {folder_name}. Expected: {ROOT_FOLDER_NAME}\n'\
                f'Actual number of files: {files_number}. Expected: {ROOT_FOLDER_NUMBER_FILES}.'

    @pytest.mark.api
    @pytest.mark.regression
    @pytest.mark.negative
    @allure.story('Get files from folder with invalid x-token')
    def test_get_files_from_root_folder_with_invalid_token(self):
        with allure.step('Get files from root folder with invalid x-token'):
            self.api.get_files_number(ROOT_FOLDER_LOCATION, TOKEN_INVALID, FORBIDDEN)

    @pytest.mark.api
    @pytest.mark.regression
    @pytest.mark.positive
    @allure.story('Get files number from specific folder')
    def test_get_files_number_from_specific_folder(self, token):
        with allure.step('Get files number from specific folder'):
            folder_name, files_number = self.api.get_files_number(SPECIFIC_FOLDER_LOCATION, token)
            assert folder_name == SPECIFIC_FOLDER_NAME and files_number == SPECIFIC_FOLDER_NUMBER_FILES,\
                f'Actual root folder name: {folder_name}. Expected: {SPECIFIC_FOLDER_NAME}\n'\
                f'Actual number of files: {files_number}. Expected: {SPECIFIC_FOLDER_NUMBER_FILES}.'

    @pytest.mark.api
    @pytest.mark.regression
    @pytest.mark.positive
    @allure.story('Get runs statuses')
    def test_get_runs_statuses(self, token):
        with allure.step('Get runs statuses'):
            statuses = self.api.get.statuses(RUNS, token, 'runs')
            assert all(status == 'Success' for status in statuses),\
                f'Actual runs statuses: {statuses}. Expected: all Success.'

    @pytest.mark.api
    @pytest.mark.regression
    @pytest.mark.positive
    @allure.story('Get analysis statuses')
    def test_get_analysis_statuses(self, token):
        with allure.step('Get analysis statuses'):
            statuses = self.api.get_statuses(ANALYSIS, token, 'analysis')
            assert all(status == 'Success' for status in statuses), \
                f'Actual analysis statuses: {statuses}. Expected: all Success.'

    @pytest.mark.api
    @pytest.mark.regression
    @pytest.mark.positive
    @allure.story('Get artifacts statuses')
    def test_get_artifacts_statuses(self, token):
        with allure.step('Get artifacts statuses'):
            statuses = self.api.get_statuses(ARTIFACTS, token, 'artifacts')
            assert all(status == 'Success' for status in statuses), \
                f'Actual artifacts statuses: {statuses}. Expected: all Success.'
