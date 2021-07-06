import pytest
import requests
import json


class TestLoginPage:

    @pytest.mark.ui
    @pytest.mark.mainpage
    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.check('check_title_presence')
    def test_check_title(self, driver):
        logging = LoginPage(driver)
        assert logging.is_block_title_present(), 'title is not present on the mainpage'

    @pytest.mark.ui
    @pytest.mark.mainpage
    @pytest.mark.smoke
    @pytest.mark.positive
    def test_post_headers_body_json(self, url, headers, json):
        self.url = 'https://httpbin.org/post'
        # Additional headers.
        self.headers = {'Content-Type': 'application/json'}
        # Body
        self.json = {'key1': 1, 'key2': 'value2'}
        # convert dict to json string by json.dumps() for body data.
        resp = requests.post(url, headers, json, dumps(payload, 4))
        # Validate response headers and body contents, e.g. status code.
        assert resp.status_code == 200
        resp_body = resp.json()
        assert resp_body['url'] == url
        # print response full body as text
        print(resp.text)
