import os
import allure
import requests
import pytest


def ScoutQueriesParser():
    pass


class BaseScout:
    def __init__(self, scout):
        self.scout = scout
        self.scout_index_documents_count()

    test_data = ScoutQueriesParser().get_queries()


class TestScout(BaseScout):

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.api_check
    @pytest.mark.scout
    @allure.story('Test index exists')
    def test_index_exist(self, scout):
        self.scout = scout
        response = scout.get.indexes()
        assert response('index' in data)

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.api_check
    @pytest.mark.parametrize("lambda_X", lambda_X1, lambda_X2, lambda_X3, lambda_X4)
    def test_refdb_index_documents_count(self):
        response = scout.get.index(filter(lambda_X))
        assert response["filtered_count"] == int(test_data["result_count"])

    @pytest.mark.smoke
    @pytest.mark.api
    @pytest.mark.api_check
    @pytest.mark.parametrize("test_data", organism, database, version)
    def test_search_per_database(self, scout, test_data):
        self.response = response
        response = scout.get_documents(
            test_data["organism"],
            test_data["database"],
            test_data["version"],
        )
        assert response["documents_count"] >= 100000
