import pytest
from utils import create_courier, login_courier, delete_courier
from data import courier_payloads

class TestCourierCreation:
    def test_create_courier(self):
        payload = courier_payloads["valid"]
        response = create_courier(payload["login"], payload["password"], payload["firstName"])
        assert response.status_code == 201
        assert response.json()["id"] is not None

        # Cleanup
        courier_id = response.json()["id"]
        delete_courier(courier_id)

    @pytest.mark.parametrize("payload", courier_payloads["invalid"])
    def test_create_courier_missing_fields(self, payload):
        response = create_courier(payload["login"], payload["password"], payload["firstName"])
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"
