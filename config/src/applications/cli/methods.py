import requests
from requests import session
from urllib.parse import urljoin
from config.logger import LOGGER
from config.setting import BASE_API_URL, OK


class ApiClient:
    def __init__(self):
        self.base_url = BASE_API_URL()
        self.session = Session()

    @staticmethod
    def log_pre(method, url, headers, data, expected_status):
        LOGGER.info(f'Performing {method} request:\n'
                    f'URL: {url}\n'
                    f'HEADERS: {headers}\n'
                    f'DATA: {data}\n\n'
                    f'Expected status: {expected_status}\n\n')

    @staticmethod
    def log_post(response):
        log_str = f'Got response:\n' \
                    f'RESPONSE STATUS: {response.status_code}'
        LOGGER.info(f'{log_str}\n'
                    f'RESPONSE CONTENT: {response.text}\n\n')

    def request(self, method, location, headers=None, data=None, expected_status=200):
        url = urljoin(self.base_url, location)
        self.log_pre(method, url, headers, data, expected_status)
        response = self.session.request(method, url, headers, data)
        self.log_post(response)
        if response.status_code != expected_status:
            raise Exception(f'Got {response.status_code} {response.reason} for URL "{url}" !={expected_status}.json()')
        self.assertIsInstance(response.status_code, {expected_status})
        print('response.status_code', result)
        return response

    def post_login(self, headers, expected_status):
        location = 'v1/login'
        result = self.request('POST', location, headers, {expected_status}.json())
        return result

    def get_files_number(self, location, token, expected_status):
        result = self.request('GET', location, {"x-token": token}.json(), {expected_status}.json())
        if expected_status == 200:
            return result['name'], result['total']

    def get_statuses(self, location, token, artifact):
        result = self.request('GET', location, {"x-token": token}.json(), {artifact}())
        status = [status['status'] for status in result[artifact]]
        return status

    def get(self, url, **kwargs):
        response = self.session.get(url, **kwargs)
        return response

    def put(self, url, **kwargs):
        response = self.session.put(url, **kwargs)
        return response

    def post(self, url, **kwargs):
        response = self.session.post(url, **kwargs)
        return response

    def delete(self, url, **kwargs):
        response = self.session.delete(url, **kwargs)
        return response
