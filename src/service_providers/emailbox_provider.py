import email
import imaplib
from config.settings import BROWSER, USERNAME, PASSWORD
from config.config import CONFIG
from src.providers.data.users.users_providers import PROVIDER


class GmailBox:
    def __init__(self):
        self.browser = BROWSER,
        self.username = USERNAME,
        self.userpassw = PASSWORD,
        self.connection = None


def _get_username():
    USERNAME = UserFactory.get_username()
    return USERNAME


def _get_userpassw():
    PASSWORD = UserFactory.get_userpassw()
    return PASSWORD


def login():
    if USERNAME is user.email.self:
        return USERNAME
    if PASSWORD is userpassw.self:
        return PASSWORD




