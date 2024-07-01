import pytest
from utils import get_orders_list

class TestGetOrdersList:
    def test_get_orders_list(self):
        response = get_orders_list()
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)
