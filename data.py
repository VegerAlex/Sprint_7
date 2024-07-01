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

order_payloads = {
    "valid": {
        "address": "test address",
        "phone": "test phone",
        "firstName": "test name",
        "lastName": "test last name",
        "metroStation": 1,
        "rentTime": 5,
        "color": ["BLACK"]
    },
    "missing_address": {
        "phone": "test phone",
        "firstName": "test name",
        "lastName": "test last name",
        "metroStation": 1,
        "rentTime": 5,
        "color": ["BLACK"]
    },
    "invalid_phone": {
        "address": "test address",
        "phone": "invalid phone",
        "firstName": "test name",
        "lastName": "test last name",
        "metroStation": 1,
        "rentTime": 5,
        "color": ["BLACK"]
    }
}

order_color_payloads = [
    ["BLACK"],
    ["GREY"],
    ["BLACK", "GREY"],
    []
]
