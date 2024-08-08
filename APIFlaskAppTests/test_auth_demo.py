from utilities.fileutilities import get_json_from_file
from utilities.apiutilities import post_api_data, get_api_data
from utilities.configparser import get_flask_app_base_url

loginJsonFile = 'loginValid.json'
baseURI = get_flask_app_base_url()
loginURLPath = 'login'
usersUrlPath = 'users'


# demo test with fetch token within test
def test_get_user_demo():
    # first login with and existing user
    login_url = baseURI + loginURLPath
    payload = get_json_from_file(loginJsonFile)
    resp = post_api_data(login_url, payload)
    print(resp.json()['token'])
    token = resp.json()['token']
    user_url = baseURI + usersUrlPath
    headers = {'x-access-token': token}
    resp_users = get_api_data(user_url, headers)
    print(resp_users.json())
