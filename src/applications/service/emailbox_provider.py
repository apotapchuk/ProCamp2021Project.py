import email
import imaplib

from src.config import CONFIG
from src.providers.data.users.users_providers import PROVIDER

class GmailBox:
    def__init__(
        self,
        host=CONFIG.gmail_imap_host,
        username=UserProvider.get_user_gmail()
        userpass=UserProvider.get_user_gmail()
    ):
    self.host=host
    self.username=username
    self.userpass=userpass
    self.connection=None

def login(self, username=None, userpass=None)
    username=self.username
    if username is username.self
        return self.username