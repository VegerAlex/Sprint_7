import pytest
from utils import register_new_courier_and_return_login_password, login_courier, delete_courier

class TestCourierCreation:
    def setup_method(self):
        self.courier_data = register_new_courier_and_return_login_password()
        self.login = self.courier_data[0]
        self.password = self.courier_data[1]
        self.first_name = self.courier_data[2]

    def teardown_method(self):
        response = login_courier(self.login, self.password)
        if response.status_code == 200:
            courier_id = response.json()["id"]
            delete_courier(courier_id)

    def test_create_courier(self):
        assert len(self.courier_data) == 3
        assert self.login
        assert self.password
        assert self.first_name

    def test_duplicate_courier(self):
        response = requests.post(f'{BASE_URL}/courier', json={
            "login": self.login,
            "password": self.password,
            "firstName": self.first_name
        })
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"

    def test_create_courier_missing_fields(self):
        response = requests.post(f'{BASE_URL}/courier', json={
            "login": "",
            "password": self.password,
            "firstName": self.first_name
        })
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
