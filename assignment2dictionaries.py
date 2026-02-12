# Creating a new dictionary
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}

print("Original dictionary:", car)
print("Length:", len(car))


# Accessing values using keys
print("Brand:", car["brand"])
print("Model:", car.get("model"))
print("Length:", len(car))


# Adding a new key
car["color"] = "Black"
print("After adding color:", car)
print("Length:", len(car))


# Updating an existing value
car["year"] = 2023
print("After updating year:", car)
print("Length:", len(car))


# Removing a key
car.pop("model")
print("After removing model:", car)
print("Length:", len(car))
