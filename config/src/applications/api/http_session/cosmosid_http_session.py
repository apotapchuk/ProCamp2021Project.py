import urllib.parse
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry


class CosmosHttpSession_retries_policy:
    CosmosHttpSession_retries_policy = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=[500, 501, 502, 503, 504],
    )
    pass


class CosmosHttpSession:
    def __init__(self, base_url):
        self.base_url = base_url
        self.user = None
        self._http_session = None
        self.expires = None
        self.token = None

    def add_headers(self, additional_headers):
        self._http_session.headers.update(additional_headers)
        return self

    def remove_headers(self):
        self._http_session.headers.remove(self)
        pass

    @property
    def http_session(self):
        if self._http_session is None:
            self._http_session = CosmosHttpSession.default_session()
        return self._http_session

    @staticmethod
    def default_session():
        _http_session = requests.Session()
        _http_session.mount("https://", HTTPAdapter(CosmosHttpSession_retries_policy))
        return _http_session

    def _prepare_url(self, url):
        return urllib.parse.urljoin(self.base_url, url)

    def get(self, url_path, *args, **kwargs):
        return self._http_session.get(self._prepare_url(url_path), *args, **kwargs)

    def put(self, url_path, *args, **kwargs):
        return self._http_session.put(self._prepare_url(url_path), *args, **kwargs)

    def post(self, url_path, *args, **kwargs):
        return self._http_session.post(self._prepare_url(url_path), *args, **kwargs)

    def delete(self, url_path, *args, **kwargs):
        return self._http_session.delete(self._prepare_url(url_path), *args, **kwargs)
