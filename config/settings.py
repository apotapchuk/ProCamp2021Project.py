import os
from src.utils import utils

ENV = os.environ.get('ENV')
BROWSER = os.environ.get('BROWSER')
BASE_URL = 'https://www.cosmosid.com/'
SOURCE_URL = 'https://www.cosmosid.com/'
LOGIN_PAGE = 'https://app.cosmosid.com/login'
BASE_API_URL = 'https://app.cosmosid.com/api/'
SITE_NAME = Metagenomics Cloud
USERNAME = UserFactory.get_username()
PASSWORD = UserProvider.get_userpassw()
USERNAME1_INVALID = f'gl{USERNAME}'
USERNAME2_INVALID = f'gl{USERNAME}'
PASSWORD1_INVALID = f'1{PASSWORD}'
PASSWORD2_INVALID = f'1{PASSWORD}'

TOKEN_INVALID = 'e93dce5c-3ddf-4e21-n345-34w4t6hgb436al'
HEADERS = utils.base64_encode_header(USERNAME, PASSWORD)
HEADERS_INVALID_USER = utils.base64_encode_header(USERNAME_INVALID, PASSWORD)
HEADERS_INVALID_PASS = utils.base64_encode_header(USERNAME, PASSWORD_INVALID)
HEADERS_INVALID_CRED = utils.base64_encode_header(USERNAME_INVALID, HEADERS_INVALID_USER)

# RESPONSE STATUS_CODES
OK = 200
UN_AUTH = 401
FORBIDDEN = 403
NOT_FOUND = 404

# ACCOUNT
ROOT_FOLDER_NAME = 'ROOT'
ROOT_FOLDER_LOCATION = 'metagenid/v2/files? =1622700773180'
ROOT_FOLDER_NUMBER_FILES = 1
SPECIFIC_FOLDER_NAME = 'Example_Datasets'
SPECIFIC_FOLDER_LOCATION = f'{ROOT_FOLDER_LOCATION}&folder_id=84c969d5-8dce-429d-8f92-44d5e28b1581'
SPECIFIC_FOLDER_NUMBER_FILES = 58

RUNS = 'metagenid/v1/files/7f4c7326-0a4e-4b56-a8d0-8ce002191672/runs?_=1622700773181'
ANALYSIS = 'metagenid/v1/runs/437ef8e4-b595-4fd8-a2f5-64221831e925/analysis?filter=total&_=1622700773184'
ARTIFACTS = 'metagenid/v1/runs/437ef8e4-b595-4fd8-a2f5-64221831e925/artifacts?_=1622700773185'


config_path = Path.home()/'PycharmProjects'/'gl-procamp_PythonProject'/'config'
config_path_json = config_path/'readers'/f'.js'
config_path_yaml = config_path/'readers'/f'.yaml'
defaults = {
    "ENV": 'uat',
    "BROWSER": 'chrome',
    "BASE_URL": 'https://www.cosmosid.com',
    "LOGIN_PAGE": 'https://app.cosmosid.com/login',
    "SUPPORTED_BROWSERS": ['chrome', 'firefox', 'edge', 'opera']
}
