import json
a = input("id")
b = input("first_name")
c = input("last_name")
d = input("email")
e = input("password")

user_dict = {"id": 1,
             "first_name": "grace",
             "last_name": "gajira",
             "email": "gracegajira01@gmail.com",
             "password": "grace@04"
             }

with open("015_register.json", "w") as my_file:
    json.dump(user_dict, my_file)
