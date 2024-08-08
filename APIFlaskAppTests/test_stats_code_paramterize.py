import pytest
from utilities.apiutilities import get_api_data
from utilities.configparser import get_flask_app_base_url

baseURI = get_flask_app_base_url()
urlPath = 'allusercount'

testData = [('application/json', 200), ('application/xml', 406), ('multipart/mixed', 406), ('text/html', 406)]


@pytest.mark.parametrize("type, status", testData)
def test_get_all_user_count_status(types, status):
    url = baseURI + urlPath
    headers = {'Accept': types}
    resp = get_api_data(url, headers)
    print(resp.status_code)
    assert resp.status_code == status
