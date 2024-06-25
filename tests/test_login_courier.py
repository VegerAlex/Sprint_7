import pytest
from utils import register_new_courier_and_return_login_password, login_courier, delete_courier

class TestCourierLogin:
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

    def test_login_courier(self):
        response = login_courier(self.login, self.password)
        assert response.status_code == 200
        assert "id" in response.json()

    def test_login_courier_missing_fields(self):
        response = login_courier("", self.password)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"
