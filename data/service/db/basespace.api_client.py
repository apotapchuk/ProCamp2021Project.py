import os
import allure
import request

from config import CONFIG


class BaseSpaseApiclient:
    def __init__(self, base_url):
        self.client_key()
        self.base_url()
        self.auth = None


def login(self, user):
    payload = {
        "username": user.email,
        "password": user.password,
        "domain": "basespase",
        "rURL": "http://basespase.illumina.com",
        "clientVars":" ",
        "originPlatformUrl": "underfined",
        "client": "basespace",
        "deviceType": " ",
        "instrumentType": " ",
        "icsVersion": " ",
        "postLoginAction": " ",
        "workgroupid": " ",
        "responseType": "underfined",
        "scope": "underfined",
        "state": "underfined",
    }
    res = request.post("https://login.illumina.com/")

def get_code(self, scope="browse_global"): (
    request.utils.quote(scope)
    requests.get("https://basespace.illumina.com/"),
    {self.base_url.illumina.com},
    f"response_type" = { },
    f"client_id" = { },
    f"scope" = { },
    login&logout = true,
    allow_redirects = false,
    cookies = {},
    timeout = (1, 120)
    )
    assert responce.status_code == 302
    code = responce.headers_store["location"]
    return code
