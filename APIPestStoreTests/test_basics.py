import allure
import requests
from typing import Dict, Tuple
from dataclasses import dataclass
from urllib.parse import urljoin


@dataclass
class Config:
    base_url: str = 'https://petstore.swagger.io/v2/pet/'
    pet_id: int = 150
    new_pet_id: int = 191
    new_pet_name: str = 'Cutie'
    new_pet_status: str = 'available'


@allure.feature('Pet Store API')
class TestPetStore:
    config = Config()

    @allure.story('Get Pet by ID')
    def test_get_pet_by_id(self):
        url, response = self.get_pet(self.config.pet_id)
        assert response.json()['id'] == self.config.pet_id, "Pet ID does not match"

    @allure.story('Get Pet Response is not Empty')
    def test_get_pet_response_is_not_empty(self):
        url, response = self.get_pet(self.config.pet_id)
        assert len(response.json()) > 0, "Response is empty"

    @allure.story('Add New Pet')
    def test_add_new_pet(self):
        url, response = self.add_pet(self.config.new_pet_id, self.config.new_pet_name, self.config.new_pet_status)
        assert response.json()['id'] == self.config.new_pet_id, "New Pet ID does not match"
        assert len(response.json()) > 0, "Response is empty"

    def get_pet(self, pet_id: int) -> Tuple[str, requests.Response]:
        url = urljoin(self.config.base_url, str(pet_id))
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, verify=False, headers=headers)
        return url, response

    def add_pet(self, pet_id: int, pet_name: str, pet_status: str) -> Tuple[str, requests.Response]:
        url = self.config.base_url
        headers = {'Content-Type': 'application/json'}
        payload: Dict[str, str] = {'id': str(pet_id), 'name': pet_name, 'status': pet_status}
        response = requests.post(url, verify=False, json=payload, headers=headers)
        return url, response
