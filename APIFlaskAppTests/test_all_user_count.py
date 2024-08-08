from utilities.apiutilities import get_api_data
from utilities.configparser import get_flask_app_base_url

baseURI = get_flask_app_base_url()
urlPath = 'allusercount'


# testing api all user count for status 200
def test_get_all_user_count_status_200():
    url = baseURI + urlPath
    headers = {'Accept': 'application/json'}
    resp = get_api_data(url, headers)
    assert resp.status_code == 200


def test_get_all_userf_count_status_406():
    url = baseURI + urlPath
    resp = get_api_data(url)
    assert resp.status_code == 406


def test_get_all_user_count_body():
    url = baseURI + urlPath
    headers = {'Accept': 'application/json'}
    resp = get_api_data(url, headers)
    data = resp.json()
    assert data['count']
    assert data['status']
    assert data['status']['message'] == 'success'


def test_get_all_user_count_time_taken():
    url = baseURI + urlPath
    headers = {'Accept': 'application/json'}
    resp = get_api_data(url, headers)
    print(resp.elapsed.total_seconds())
    assert (resp.elapsed.total_seconds()) < 1
