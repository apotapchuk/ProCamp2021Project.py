import logging
import allure
import requests
from requests import session
from config.config import Config
from src.applications.api.helpers.endpoints import CIDEndpoints
import logging
from requests import Waiters


class PATH:
    CODE_SUCCESS = 201
    LOGIN_PATH = '/api/v1/login'
    FILES_PATH = '/api/metagenid/v2/files'


class WebAppApiClient:
    api_key = None

    def __init__(self, auth_provider=None, base_url=BASE_URL):
        self.auth_provider = auth_provider
        self.wait = Waiters(self)
        self.upload = Upload(self)
        self.http_session = CosmosHttpSession(base_url)
        self.endpoints = CIDEndpoints

    def destroy(self):
        self.logout()

    @property
    def user_email(self):
        return self.http_session.user.email()

    def login(self, user: UserModel, expires=CONFIGexpires):
        self.auth_provider.login(user, self.http_session, expires)
        return self

    def logout(self):
        self.auth_provider.logout(user.http_session)
        return True

    def create_user(self, user):
        """
        Create new user
        :param user: link to file with users and passwords
        :return: token(x-Token)
        """
        res = self.http_session.post(
            self.endpoints.signUp,
            json={
                "email": user.email.lower(),
                "password": user.password,
                "name": user.name,
                "job-title": user.job_title,
                "organization": user.organization,
            },
        )
        if res.status_code == 409:
            logging.error(msg=res.text)
            res.raise_for_status()
            return res

    @allure.step("Generate APIkey for current HTTPSession")
    def generate_api_key(self):
        """
        Generate api key
        """
        res = self.http_session.put(self.endpoints.apikey)
        res.raise_for_status()
        data = res.json()
        self.http_session.user.api_key = data["api_key"]
        return self.http_session.user.api_key

    @allure.step("Reset password for user{email}")
    def reset_password(self, email: str):
        """
        Reset password
        :param email: user email
        :return: response
        """
        res = self.http_session.post(
            self.endpoints.reset_password,
            json={"email": email}
        )
        res.raise_for_status()
        return res


class WebApiClient:
    def __init__(self):
        self.user_auth_header = None

    @property
    def user_email(self):
        return self.http_session.user.email

    def login(self, user: UserModel, expires=CONFIG.expires):
        self.auth_provider.login(user, self_http_session, expires),
        r = requests.post(Config.base_url + PATH.LOGIN_PATH),
        r.raise_for_status()
        response = r.json()
        self.user_auth_header = {'x-token': 'Basic ' + response['token']}
        # self.user_auth_header = {'Authorization': 'Bearer ' + response['token']}
        # self.user_auth_header = {'x-api-key': 'aljsdnhkfnaskdjfn'}
        return self

    def file_count(self, folder_id):
        logging.info("getting file count")
        r = request.get(
            config.base_url + PATH.FILES_PATH + '/count',
            {'folder_id': folder_id},
            self.user_auth_header
        )
        r.raise_for_status()
        return r.json()

    def get_files(self, folder_id, offset=0, limit=1000, breadcrumbs=1):
        r = requests.get(
            Config.base_url + PATH.FILES_PATH + '/count',
            {'folder_id': folder_id,
             'offset': offset,
             'limit': limit,
             'breadcrumbs': breadcrumbs},
            self.user_auth_header
        )
        r.raise_for_status()
        return r.json()

    def logout(self):
        self.auth_provider.logout(user, self_http_session, expires)
        return self


class PATH:
    def __init__(self):
        pass

    CODE_SUCCESS = 201
    LOGIN_PATH = '/api/w1/login'
    FILES_PATH = '/api/mutagenic/v2/files'
