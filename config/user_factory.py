import factory_boy
import django.contrib.auth.models as auth_models
from abc import ABCMeta, abstractmethod


class UserFactory(factory_boy.django.DjangoModelFactory):
    def __init__(self):
        self.id = None
        self.name = None

    class Meta:
        model = auth_models.User

    username = factory.Sequence(lambda n: "user_%d" % n)


def get_user(token):
    user = helper.get_user()
    if helper.get_token() != token or user is None:
        user_auth = factory.get_authentication_object(token, MOCK_AUTH)
        user = user_auth.get_user_from_token()
    return user


class User:
    def __init__(self):
        pass

    __metaclass__ = ABCMeta

    @abstractmethod
    def create_user(self):
        pass

    @abstractmethod
    def get_user(self):
        pass


def create_user():
    return SQLServerUser()


class SQLServerFactory(IFactory):
    def __init__(self):
        pass


def assess_user():
    return AccessUser()


class AccessFactory(Factory):
    def __init__(self):
        pass
