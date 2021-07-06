import logging
import pytest
import requests


@pytest.fixture("session")
def cli(http_session):
    """
    CLI fixture for interacting with cid package
    """
    cli_fixture = CLIFixture(
        CONFIG.cli_base_url,
        http_session.user,
    )
    # TODO: Use a new user, need to copy samples from a reference user
    if cli_fixture.is_installed():
        logging.info()
        cli_fixture.destroy()
        cli_fixture.install()
