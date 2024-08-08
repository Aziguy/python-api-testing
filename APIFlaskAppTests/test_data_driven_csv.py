import pytest
from utilities.fileutilities import get_csv_data_as_dict, get_data_as_tuple
from utilities.apiutilities import post_api_data
from utilities.configparser import get_flask_app_base_url

baseURI = get_flask_app_base_url()
dataFile = 'registerApiData.csv'
urlPath = 'register'
dataFileWithStatus = 'registerApiDataWithStatus.csv'
getData = get_data_as_tuple(dataFileWithStatus)


# datadriven test from datafile, inserting all data in single test
def test_data_driven_reg_api():
    url = baseURI + urlPath
    payload_list = get_csv_data_as_dict(dataFile)
    for dataLines in payload_list:
        print(dataLines)
        resp = post_api_data(url, dataLines)
        assert resp.status_code == 201
        data = resp.json()
        print(data)
        assert data['id']


# datadriven test from datafile, uses Pytest paramterization, separate test for each row from data file
@pytest.mark.parametrize("input, respStatus", get_data_as_tuple(dataFileWithStatus))
def test_data_driven_parametrized(inputs, resp_status):
    url = baseURI + urlPath
    print(getData)
    print(inputs, resp_status)
    keys = ['email', 'password']
    request_dict = dict(zip(keys, inputs))
    print("Request Dict: ", request_dict, resp_status)
    # resp = postApiData(url, requestDict)
    # assert resp.status_code == int(respStatus)
