import factory_boy
import django.contrib.auth.models as auth_models
from abc import ABCMeta, abstractmethod


class UserFactory(factory_boy.django.DjangoModelFactory):
    def __init__(self):
        self.id = None
        self.username = None
        self.userpassw = None

    class Meta:
        model = auth_models.User

    username = factory.Sequence(lambda n: "user_%d" % n)


def get_user(token):
    user = helper.get_user()
    if helper.get_token() != token or user is None:
        user_auth = factory.get_authentication_object(token, MOCK_AUTH)
        user = user_auth.get_user_id_from_token()
    return user


class User:
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def create_user(self):
        return SQLServerUser(get_userid, get_username, get_userpassw)

    @abstractmethod
    def get_user_id(self):
        self.userid = new_user.id

    def get_user_username(self):
        self.username = new_user.email

    def get_user_userpassw(self):
        self.userpassw = new_user.passw


class SQLServerFactory(IFactory):
    def __init__(self):
        pass


def assess_user():
    return AccessUser(new_user.id, new_user.email, new_user.passw)


class AccessFactory(Factory):
    def __init__(self):
        pass
