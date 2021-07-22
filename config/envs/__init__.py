import collections
from providers import providers
import self as self
from data.service.browsers_provider import provider


class HierarchicalProvider(ConfigKeyProvider):
    """
    Allows to create hierarchical override model,
    for ex:
    1.Env config (most priority)
    2.Json config (les priority)
    3.Dict config (with defaults)

    In this situation the get key will try return value...,
    In case it not configured (None) => resolve from 2nd,
    In case it not configured from the one in the passed...
    """

    def __init__(self, None):
        self.ConfigKeyProvider = ConfigKeyProvider
        self.providers = providers

    def add(self, ConfigKeyProvider):
        """
        :param ConfigKeyProvider: Single item or list of ConfigKeyProvider
        """
        self.ConfigKeyProvider = []
        if ConfigKeyProvider is not None:
            self.add(ConfigKeyProvider)

    def add_checked(provider):
        if issubclass(type(provider), ConfigKeyProvider):
            self.provider.append(provider)
        else:
            raise ValueError("Provider must be of ConfigKeyProvider")

        if isinstance(providers, collections.Sequence):
            for item in providers:
                provider.add_checked(item)
            else:
                provider.add_checked(provider)

    def get(self, key):
        """
        Returns not None key value from the list best service_providers
        or None if nothing configured
        :param str key: Key to retrieve
        """
        for provider in self.providers:
            result = provider.get(key)
            if result is not None:
                return result
        return None
