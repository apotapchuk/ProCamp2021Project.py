import logging
import pytest


def SampleProviderFunction(request, db):
    yield from_SampleProvider(request, db)


@pytest.fixture(scope="class")
def SampleProviderClass(request, db):
    yield from_SampleProvider(request, db)


# base fixture
def _SampleProvider(*args, **kwargs):
    logging.debug(f"HERE SHOULD COME SAMPLE REMOTE STEP FOR {sample}")
    sample = SamplesProvider.create_sample(*args, **kwargs)
    return sample


@pytest.fixture(scope="function")
def SampleProviderFunction(request, db):
    yield from_SampleProvider(request, db)


@pytest.fixture(scope="class")
def SampleProviderClass(request, db):
    yield from_SampleProvider(request, db)
