import os
from pathlib import Path
import yaml

HOME_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
BASE_URL = 'https://www.cosmosid.com/'
LOGIN_PAGE = 'https://app.cosmosid.com/login'
BROWSER = os.environ.get('BROWSER', 'chrome')
config_path = Path.home()/'PycharmProjects'/'gl-procamp_PythonProject'/'Core'
config_path_json = config_path/'env-configs'/f'.js'
config_path_yaml = config_path/'config.yaml'
defaults = {
    "ENV": 'uat',
    "BROWSER": 'chrome',
    "BASE_URL": "https://www.cosmosid.com",
    "LOGIN_PAGE": "https://app.cosmosid.com/login",
    "SUPPORTED_BROWSERS": ["chrome", "firefox", "edge", "opera"]
}

class Config:
    def __init__(self):
        self.config_path = config_path(os.path.join(HOME_PATH, 'core', 'config.yaml'))
        self.base_url = config_path(os.path(BASE_URL, "BASE_URL"))
        self.port = "port"
        self.user = "user"
        self.password = "password"
        self.timeout = "timeout"

    @classmethod
    def get_config(cls, key: str):
        """
        Get configuration hierarchically from different sources
        """
        final_config = Config()
        config = final_config.__dict__.keys()
        env_var_config = cls._get_config_from_env_var()
        json_config = cls._get_config_from_file(cls.config_path_json)
        yaml_config = cls._get_config_from_file(cls.config_path_yaml)
        config_providers = [env_var_config, json_config, yaml_config, cls.defaults]
        for provider in config_providers:
            result = provider.get(key)
            if result is not None:
                return result
            return config

    @classmethod
    def _get_config_from_env_var(cls):
        """
        Get configuration from environment variables
        """
        config = {}
        for key, value in cls.defaults.items():
            if key in os.environ:
                config[key] = os.environ[key]
            return config

    @classmethod
    def _get_config_from_file(cls, file_path):
        """
        Get configuration from file
        """
        with open(file_path, encoding='utf8') as fn:
            config = yaml.load(fn)
        return config
