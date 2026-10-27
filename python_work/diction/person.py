person = {
    'first_name': 'Fred',
    'last_name': 'Smith',
    'age': 29,
    'city': 'Medford',
    }

print("The attributes of a person.")
for key, value in person.items():
    print(f"This persons {key.title()} is {value}.")
