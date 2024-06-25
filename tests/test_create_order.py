import pytest
from utils import create_order

class TestOrderCreation:
    def setup_method(self):
        self.order_data = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": ["BLACK"]
        }

    def test_create_order(self):
        response = create_order(self.order_data)
        assert response.status_code == 201
        assert "track" in response.json()
