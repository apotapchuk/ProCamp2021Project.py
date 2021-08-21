import time
from _pytest import pytest
from scout_client import scout
from src.tools.helpers.parsers.scout_queries_parsers import ScoutQueriesParser
import pytest
from src.config import CONFIG
from scout_client import scout
from src.tools.helpers.parsers.scout_queries_parser import QueriesParser


class ScoutClient:
    def __init__(self):
        self.scout_base_url = SCOUT_BASE_URL()

    @pytest.fixture("class")
    def scout_config_base_url():
        return scout(CONFIG_SCOUT_BASE_URL)

    RestAssured.requestSpecification = requestSpecification
    RestAssured.responseSpecification = responseSpecification

    @pytest.fixture("class")
    @pytest.mark.smoke
    @pytest.mark.admin
    @pytest.mark.admin_login
    @pytest.mark.ui
    def test_admin_login(admin_app):
        assert admin_app.is_logged_in()

    @pytest.mark.regression
    @pytest.mark.admin
    @pytest.mark.admin_user_mngmnt
    @pytest.mark.ui
    def test_user_table_is_not_empty(admin_app):
        admin_app.users_page.open()
        time.sleep(1)  # TODO:add proper wait
        assert (
            admin_app.users_page.users_table.check_user_list_is_not_empty()
        ), f"users are:{admin_app.users_page.users_table.get_users(limit=100)}"
