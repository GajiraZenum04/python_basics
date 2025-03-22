import json


data_dict = {
        "id": 3,
        "name": "Grace",
        "gender": "Female",
        "department": "Mass Communication",
        "school": "Ambrose Alli University",

        }

with open("013_data.json", "w") as my_file:
    json.dump(data_dict, my_file)



