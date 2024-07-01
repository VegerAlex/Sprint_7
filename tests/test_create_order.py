import pytest
from utils import create_order
from data import order_payloads


class TestOrderCreation:
    def test_create_order(self):
        payload = order_payloads["valid"]
        response = create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()

    def test_create_order_missing_address(self):
        payload = order_payloads["missing_address"]
        response = create_order(payload)
        assert response.status_code == 400
        assert "message" in response.json()

    def test_create_order_invalid_phone(self):
        payload = order_payloads["invalid_phone"]
        response = create_order(payload)
        assert response.status_code == 400
        assert "message" in response.json()
