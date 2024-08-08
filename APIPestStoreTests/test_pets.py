import logging
from typing import Tuple, Dict, Any
from utilities.configparser import get_pet_api_url
from utilities.utils import get_api_data, put_data, delete_data

LOGGER = logging.getLogger(__name__)
PET_ID = '150'


def test_get_pet_by_id_response() -> None:
    """
    Test case to verify the response of the 'Get Pet by ID' API.
    """
    url = f"{get_pet_api_url()}{PET_ID}"
    data, resp_status, time_taken = get_api_data(url)
    assert data['id'] == int(PET_ID)
    assert resp_status == 200
    LOGGER.info("Time Taken: %.2f seconds", time_taken)


def test_update_pet() -> None:
    """
    Test case to update an existing pet.
    """
    payload: Dict[str, Any] = {"id": int(PET_ID), "name": "Cutie", "status": "pending"}
    data, resp_status, time_taken = put_data(get_pet_api_url(), payload)
    LOGGER.info("API call done")
    assert data['id'] == int(PET_ID)
    LOGGER.debug("Response data: %s", data)


def test_delete_pet_by_id() -> None:
    """
    Test case to delete a pet by its ID.
    """
    url = f"{get_pet_api_url()}{PET_ID}"
    optional_headers: Dict[str, Any] = {'api_key': 'apiKeys123'}
    data, resp_status, time_taken = delete_data(url, optional_headers)
    LOGGER.debug("Response data: %s", data)
    assert data['message'] == PET_ID
    assert data['code'] == 200


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    test_get_pet_by_id_response()
    test_update_pet()
    test_delete_pet_by_id()
