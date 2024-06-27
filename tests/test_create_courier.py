import pytest
from utils import create_courier
from data import courier_payloads

class TestCourierCreation:
    def test_create_courier(self, courier_data):
        assert len(courier_data) == 3
        assert courier_data[0]  # login
        assert courier_data[1]  # password
        assert courier_data[2]  # first_name

    @pytest.mark.parametrize("payload", courier_payloads['invalid'])
    def test_create_courier_missing_fields(self, payload):
        response = create_courier(payload['login'], payload['password'], payload['firstName'])
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
