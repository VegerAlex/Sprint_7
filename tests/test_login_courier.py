import pytest
from utils import login_courier


class TestCourierLogin:
    def test_login_courier(self, courier_data):
        login, password, _ = courier_data
        response = login_courier(login, password)
        assert response.status_code == 200
        assert "id" in response.json()

    @pytest.mark.parametrize("login, password", [
        ("", "password"),
        ("login", "")
    ])
    def test_login_courier_missing_fields(self, login, password):
        response = login_courier(login, password)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    def test_login_courier_invalid_credentials(self):
        response = login_courier("invalid_login", "invalid_password")
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

