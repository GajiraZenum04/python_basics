import json

with open("009_data.json", "r") as json_file:
    car = json.load(json_file)

    print(car["brand"])

    print(car.get("year"))

    print(car["features"])

    print(car["engine"]["horsepower"])

car["year"] = 2025
print(car)
    
car["speed"] = "180km/h"
print(car)

car.update({"country": "japan"})
print(car)

del car["color"]
print(car)
    
Model = car.pop("model")
print(car)

with open("011_new_data.json", "w") as new_json:
    json.dump(car, new_json)

print(car)

print(len(car))
print(car.keys())
print(car.values())
print(car.items())

for key in car.keys():
    print(key)

for key, value in car.items():
    print(key, value)


