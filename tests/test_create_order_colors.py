import pytest
from utils import create_order
from data import order_color_payloads

class TestOrderCreationColors:
    @pytest.mark.parametrize("color", order_color_payloads)
    def test_create_order_with_color(self, color):
        payload = {
            "address": "test address",
            "phone": "test phone",
            "firstName": "test name",
            "lastName": "test last name",
            "metroStation": 1,
            "rentTime": 5,
            "color": color
        }
        response = create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()
