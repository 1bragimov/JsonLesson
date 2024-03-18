import json

user = {"name": "John",
        "email": "<EMAIL>",
        "username": {
            "first": "John",
            "last": "Smith",
            "country": "USA"
        }
        }

# print(type(user))

with open("user.json", "w") as file_json:
    json.dump(user, file_json)
