# nesting a list of dictionaries

person_1 = {'first': 'mary', 'last': 'nelson', 'age': 48, 'location': 'bronx'}
person_2 = {'first': 'sam', 'last': 'donaldson', 'age': 45, 'location': 'brooklyn'}
person_3 = {'first': 'alex', 'last': 'davis', 'age': 49, 'location': 'queens'}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first']} {person['last']}"
    print(f"\nInformation for {full_name.title()}")
    print(f"\tFirst Name: {person['first'].title()}")
    print(f"\tLast Name: {person['last'].title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tLocation: {person['location'].title()}")
