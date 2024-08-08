import requests
import json
from typing import Dict, Any, Optional


def get_api_data(url: str, optional_headers: Optional[Dict[str, Any]] = None) -> requests.Response:
    """
    Performs a GET request to the specified URL with optional additional headers.

    Args:
        url (str): The URL to send the GET request to.
        optional_headers (Dict[str, Any], optional): Additional headers to include in the request. Defaults to None.

    Returns:
        requests.Response: The response object from the GET request.
    """
    headers = {'Content-Type': 'application/json'}
    headers = {**headers, **optional_headers} if optional_headers else headers
    response = requests.get(url, verify=False, headers=headers)
    print("\nRequestURL:", url)
    print("request header:", response.request.headers)
    print("response header:", response.headers)
    return response


def post_api_data(url: str, body: Dict[str, Any]) -> requests.Response:
    """
    Performs a POST request to the specified URL with the given request body.

    Args:
        url (str): The URL to send the POST request to.
        body (Dict[str, Any]): The request body as a dictionary.

    Returns:
        requests.Response: The response object from the POST request.
    """
    headers = {'Content-Type': 'application/json'}
    print("\nReqURL:", url)
    print("ReqBody:", json.dumps(body))
    return requests.post(url, verify=False, json=body, headers=headers)


def delete_api_data(
    url: str, body: Dict[str, Any], optional_headers: Optional[Dict[str, Any]] = None
) -> requests.Response:
    """
    Performs a DELETE request to the specified URL with the given request body and optional additional headers.

    Args:
        url (str): The URL to send the DELETE request to.
        body (Dict[str, Any]): The request body as a dictionary.
        optional_headers (Dict[str, Any], optional): Additional headers to include in the request. Defaults to None.

    Returns:
        requests.Response: The response object from the DELETE request.
    """
    headers = {'Content-Type': 'application/json'}
    headers = {**headers, **optional_headers} if optional_headers else headers
    print("\nReqURL:", url)
    print("ReqBody:", json.dumps(body))
    response = requests.delete(url, json=body, headers=headers)
    return response
