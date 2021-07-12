import logging
import pytest

from src.config import CONFIG
from src.applications.cli.cosmosid_cli import CliFixture


@pytest.fixture('session')
def cli(regular_user_api_session):
    """
    CLI fixture for interacting with cli package
    """
    regular_user_api_session = regular_user_api_session(self)
    CLIFixture(
        CONFIG.cli_base_url,
        regular_user_api_session.http_session.user,
        CONFIG.cli_install_params,
        CONFIG.cli_version,
        )

        if cli_fixture.is_installed():
            logging.INFO()
            cli_fixture.destroy()
            cli_fixture.install()
