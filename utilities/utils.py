import allure
import requests
import json
from typing import Tuple, Dict, Any


def get_api_data(url: str) -> Tuple[Dict[str, Any], int, float]:
    """
    Performs a GET request to the specified URL and returns the response data, status code, and time taken.

    Args:
        url (str): The URL to send the GET request to.

    Returns: Tuple[Dict[str, Any], int, float]: A tuple containing the response data as a dictionary, the status
    code, and the time taken to execute the request.
    """
    headers = {'Content-Type': 'application/json'}
    print(f"RequestURL: {url}")
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    assert len(data) > 0, "Empty response!"
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken


@allure.step('Doing Post Data')
def put_data(url: str, body: Dict[str, Any]) -> Tuple[Dict[str, Any], int, float]:
    """
    Performs a PUT request to the specified URL with the given request body.

    Args:
        url (str): The URL to send the PUT request to.
        body (Dict[str, Any]): The request body as a dictionary.

    Returns: Tuple[Dict[str, Any], int, float]: A tuple containing the response data as a dictionary, the status
    code, and the time taken to execute the request.
    """
    headers = {'Content-Type': 'application/json'}
    print(f"RequestURL: {url}")
    print(f"ReqBody: {json.dumps(body)}")
    response = requests.put(url, verify=False, json=body, headers=headers)
    data = response.json()
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken


def delete_data(url: str, optional_headers: Dict[str, Any] = None) -> Tuple[Dict[str, Any], int, float]:
    """
    Performs a DELETE request to the specified URL with optional additional headers.

    Args:
        url (str): The URL to send the DELETE request to.
        optional_headers (Dict[str, Any], optional): Additional headers to include in the request. Defaults to None.

    Returns: Tuple[Dict[str, Any], int, float]: A tuple containing the response data as a dictionary, the status
    code, and the time taken to execute the request.
    """
    headers = {'Content-Type': 'application/json'}
    print(f"RequestURL: {url}")
    headers = {**headers, **optional_headers} if optional_headers else headers
    response = requests.delete(url, verify=False, headers=headers)
    print(response.request.headers)
    data = response.json()
    time_taken = response.elapsed.total_seconds()
    return data, response.status_code, time_taken
