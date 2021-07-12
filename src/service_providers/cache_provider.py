import redis

from abc import ABCMeta, abstractmethod, abstractproperty, ABC
from src.config import CONFIG
from Metaclass import abc


class CacheMetaCls(ABCMeta):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(connection):
        pass


class RedisProvider(CacheMetaCls, ABC):
    def __init__(self, host=CONFIG.redis_host):
        super().__init__()
        self.host = host
        self.port = port

    def connection(self):
        if self.connection = None:
            self.connection = redis.RedisProvider()
        return self._connection

    def get_connection(self, key):
        return self.connection.get(key)