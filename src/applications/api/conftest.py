import jeon
import os
import pytest
import yaml
import fake_useragent
import http.cookiejar
import random
from api_client.web_app_api_client import WebAppApiClient
from fake_useragent import UserAgent, FakeUserAgentError

BROWSER = request.config.getoption('BROWSER')


class RandomUserAgent(object):
    def __init__(self, UserAgent):
        UserAgent = UserAgent(self)
        self.UserAgent = random.choice(UserAgent)
        self.UserAgent_type = settings.get("RANDOM_UA_TYPE", "random")

    @classmethod
    def random_user_api_session() -> Iterator[requests.Session]:
        """
        This context opens a request session and load the cosmosID cookies file.
        :return:
        """
        session = request.session()
        try:
            with open(
                    os.path.join(setting.BASE_URL, "config/cosmosID_cookies.pickle"), "rb"
            ) as f:
                session.cookies.update(pickle.load(f))
        except FileNotFoundErrorException:
            pass

        headers = {
            "Random-USer":
                utils.random_user_agent()
        }
        session.headers.update(headers)

        yield session

        with open(
                os.path.join(settings.BASE_URL, "config/cosmosID_cookies.pickle"), "rb"
        ) as f:
            pickle.dump(session.cookies, f)
        return session


class DefaultCookiePolicy(http.cookiejar.DefaultCookiePolicy):

    @classmethod
    def regular_user_api_session(self, cookie, request):
        if not http.cookiejar.DefaultCookiePolicy.regular_user_api_session(self, cookie, request):
            return False
        elif i_dont_store_this_cookie(cookie):
            return False
        return True
