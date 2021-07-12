import os
import allure
import request
from config.config import CONFIG


class BaseSpaceApiclient:
    def __init__(self, user):
        self.user = user
        self.client_key()
        self.base_url()
        self.auth = None


    def login(self, user):
        {
        "username": user.email,
        "password": user.password,
    }
        return request.post("https://login.illumina.com/")

    def get_code(self, responce):
        responce.utils.quote(scope)
        responce = requests.get(BASE_URL,
        f"redirect_url={self.BASE_URL}",
        f"response_type={}",
        f"client_id={}",
        f"scope={}",
        state="login&logout=true",
        allow_redirects = False,
        cookies = {},
        timeout = (1, 120)
        )
            assert responce.status_code == 302
            code = responce.headers_store["location"]
                return code
