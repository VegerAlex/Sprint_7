import pytest
from utils import register_new_courier_and_return_login_password, login_courier, delete_courier

@pytest.fixture(scope='session')
def courier_data():
    data = register_new_courier_and_return_login_password()
    yield data
    if data:
        login, password, _ = data
        response = login_courier(login, password)
        if response.status_code == 200:
            courier_id = response.json()["id"]
            delete_courier(courier_id)
