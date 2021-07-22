import os
import collections
import providers

import ConfigKeyProvider from HierarchicalProvider

class Config(BaseConfig):
def__init__(self):
config_path = f"env_configs/{os.enwiron}"
if os.environ["TARGET"] == "qa"
    else "specifications/scout_index/qa.yaml"
)
app_env = ConfigFromEnvProvider()
app_json_conf = ConfigFromSimpleJsonProvider
app_defaults = ConfigFromDictProvider(
"USERS_DATA_PATH": "data/users"
"SAMPLES_DATA_PATH": "data/samples"
"SCOUT_DATA_PATH": f"specifications/workfow"
"SCOUT_SPECS_PATH": "scout_spec_path",
"AWS_UPLOADS_BUCKET": "cosmosid_aws"
"AWS_SECRET_ACCESS_KEY":
"AWS_ACCESS_KEY_ID": "..."
"AWS_DEFAULT_REGION": "US -..."
"AWS_S3_ENDPOINT_URL": "https://..."
"ADMIN_BASE_UPL": "https://..."
"UTOOL_BASE_URL":
"CLI_BASE_URL":
"CLI_INSTALL_PARAMS":
"CLI_VERSION":
"SCOUT_BASE_URL":
"ILLUMINA_CLIENTT_..."
"REDIS_PORT": "6379" +
"REDIS_HOST": ".."