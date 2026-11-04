# nesting a list of dictionaries

pet_1 = {'name': 'itchy','owner': 'mary', 'species': 'dog', 'weight': 9, 'location': 'bronx', 'color': 'golden'}
pet_2 = {'name': 'scratchy','owner': 'sam', 'species': 'cat', 'weight': 4, 'location': 'brooklyn', 'color': 'black'}
pet_3 = {'name': 'blueberry','owner': 'alex', 'species': 'bird', 'weight': 1, 'location': 'queens', 'color': 'blue'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    heading = f"This is {pet['name']} cared for by {pet['owner']}"
    print(f"\n{heading.title()}")
    print(f"\tPet Name: {pet['name'].title()}")
    print(f"\tCared for by: {pet['owner'].title()}")
    print(f"\tSpecies: {pet['species']}")
    print(f"\tWeight: {pet['weight']}lbs")
    print(f"\tLocation: {pet['location'].title()}")
    print(f"\tColor: {pet['color'].title()}")
