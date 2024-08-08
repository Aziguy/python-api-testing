import time
import pytest
import random
from utilities.apiutilities import post_api_data, delete_api_data
from utilities.fileutilities import get_json_from_file
from utilities.configparser import get_flask_app_base_url

baseURI = get_flask_app_base_url()
regUrlPath = 'register'
loginUrlPath = 'login'
delUrlPath = 'delete'
registerJsonFile = 'resgisterApiValid.json'
randNum = random.randint(0, 1000)
eMail = 'automateUser@auto' + str(randNum)
password = '1234'


@pytest.fixture(scope='module')
def reg_user():
    payload = get_payload_dict_reg_api(eMail, password)
    reg_url = baseURI + regUrlPath
    reg_response = post_api_data(reg_url, payload)
    assert reg_response.status_code == 201
    assert reg_response.json()['id']
    data = reg_response.json()
    print("Inside Fixture SETUP")
    yield data  # anything after this stmt, will run as part of teardown, or after the test function is executed.
    # time.sleep(5)
    print("Inside Fixture YIELD")
    del_url = baseURI + delUrlPath
    login_url = baseURI + loginUrlPath
    login_resp = post_api_data(login_url, payload)
    token = login_resp.json()['token']
    headers = {'x-access-token': token}
    payload = {"id": reg_response.json()['id']}
    del_resp = delete_api_data(del_url, payload, headers)
    assert del_resp.status_code == 200
    assert del_resp.json()['id'] == reg_response.json()['id']


def test_login_correct_creds(reg_user):
    payload = get_payload_dict_reg_api(eMail, password)
    url = baseURI + loginUrlPath
    resp = post_api_data(url, payload)
    assert resp.status_code == 200


def test_login_empty_password(reg_user):
    reg_user_data = reg_user
    payload = get_payload_dict_reg_api(eMail, '')
    url = baseURI + loginUrlPath
    resp = post_api_data(url, payload)
    assert resp.status_code == 401


def get_payload_dict_reg_api(email=None, pwd=None):
    payload = get_json_from_file(registerJsonFile)
    payload['email'] = email
    payload['password'] = pwd
    return payload
