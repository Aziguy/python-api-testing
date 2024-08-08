import pytest
from utilities.fileutilities import get_json_from_file
from utilities.apiutilities import post_api_data, get_api_data
from utilities.configparser import get_flask_app_base_url


loginJsonFile = 'loginValid.json'
baseURI = get_flask_app_base_url()
loginURLPath = 'login'


@pytest.fixture
def get_token():
    login_url = baseURI + loginURLPath
    payload = get_json_from_file(loginJsonFile)
    resp = post_api_data(login_url, payload)
    print(resp.json()['token'])
    token = resp.json()['token']
    yield token
