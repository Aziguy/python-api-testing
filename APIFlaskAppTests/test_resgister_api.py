from utilities.apiutilities import post_api_data
from utilities.fileutilities import get_json_from_file
from utilities.configparser import get_flask_app_base_url

baseURI = get_flask_app_base_url()
urlPath = 'register'
registerjsonFile = 'resgisterApiValid.json'


# testing register API with body from file
def test_register_api():
    url = baseURI + urlPath
    payload = get_json_from_file(registerjsonFile)
    resp = post_api_data(url, payload)
    print(resp.json())
    assert resp.status_code == 201
