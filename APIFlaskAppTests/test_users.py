import json

import pytest
from utilities.fileutilities import get_json_from_file
from utilities.apiutilities import post_api_data, get_api_data
from utilities.configparser import get_flask_app_base_url

# loginJsonFile = 'loginValid.json'
baseURI = get_flask_app_base_url()
# loginURLPath = 'login'
usersUrlPath = 'users'


# @pytest.fixture
# def get_token():
#     loginURL = baseURI + loginURLPath
#     payload = get_json_from_file(loginJsonFile)
#     resp = post_api_data(loginURL, payload)
#     print(resp.json()['token'])
#     token = resp.json()['token']
#     yield token


# test get users with fixtures
def test_get_users(get_token):
    token = get_token
    users_url = baseURI + usersUrlPath
    headers = {'x-access-token': token}
    resp_users = get_api_data(users_url, headers)
    print(json.dumps(resp_users.json(), indent=4))
    assert resp_users.json()['users'][0]['email']
