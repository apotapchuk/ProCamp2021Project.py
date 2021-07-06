import pytest
from src.config import CONFIG
from scout_client import scout
from src.tools.helpers.parsers.scout_queries_parser import ScoutQueriesPqrser

ConfigFromSimpleJsonProvider = HierarchalProvider


class Config(BaseConfig):
    def __init__(self):
        self.config_path = f'env_configs/{os.environ[TARGET]}.json'
        self.scout_spec_path = (
            f'specifications/scout_index/{os.environ}'
            if os.environ['TARGET'] == "prod"
            else "specifications/scout_index/dev.yaml"
        )
        app_env = ConfigFromEnvProvider()
        app_json_conf = ConfigFronSimpleJsonProvider()
        app_default = ConfigFromDictProvider(ConfigProvider)
    {
        "USERS_DATA_PATH": "data/users",
        "SAMPLES_DATA_PATH": "data/data/samples",
        "SCOUT_DATA_PATH": "data/scout/search",
        "WORKFLOW_SPECS_PATH": f'specification/workflow',
        "SCOUT_SPECS_PATH": f'scout_spec_path'
    }

    @pytest.fixture(scope="class")
    def scout():
        return scout(CONFIG.SCOUT_BASE_URL)
