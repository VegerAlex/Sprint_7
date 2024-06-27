courier_payloads = {
    "valid": {
        "login": "testlogin",
        "password": "testpassword",
        "firstName": "testname"
    },
    "invalid": [
        {"login": "", "password": "testpassword", "firstName": "testname"},
        {"login": "testlogin", "password": "", "firstName": "testname"},
        {"login": "testlogin", "password": "testpassword", "firstName": ""}
    ]
}

order_payloads = [
    ({"color": ["BLACK"], "address": "test address", "phone": "test phone", "firstName": "test name", "lastName": "test last name", "metroStation": 1, "rentTime": 5}, 201),
    ({"color": ["BLACK"], "address": "", "phone": "test phone", "firstName": "test name", "lastName": "test last name", "metroStation": 1, "rentTime": 5}, 400)
]
