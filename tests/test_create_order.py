import pytest
from utils import create_order
from data import order_payloads

class TestOrderCreation:
    @pytest.mark.parametrize("payload, expected_status", order_payloads)
    def test_create_order(self, payload, expected_status):
        response = create_order(payload)
        assert response.status_code == expected_status
        if expected_status == 201:
            assert "track" in response.json()
        elif expected_status == 400:
            assert "message" in response.json()