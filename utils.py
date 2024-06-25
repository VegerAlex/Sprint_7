import requests
import random
import string

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def create_courier(login, password, first_name):
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return requests.post(f'{BASE_URL}/courier', json=payload)

def login_courier(login, password):
    payload = {
        "login": login,
        "password": password
    }
    return requests.post(f'{BASE_URL}/courier/login', json=payload)

def delete_courier(courier_id):
    return requests.delete(f'{BASE_URL}/courier/{courier_id}')

def create_order(data):
    return requests.post(f'{BASE_URL}/orders', json=data)

def get_orders_list():
    return requests.get(f'{BASE_URL}/orders')

def register_new_courier_and_return_login_password():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(f'{BASE_URL}/courier', json=payload)
    if response.status_code == 201:
        return [login, password, first_name]
    return []
