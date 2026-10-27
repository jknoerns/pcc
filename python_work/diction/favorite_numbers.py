favorite_numbers = {
    'johann': 5,
    'toprak': 7,
    'luca': 10,
    'diogo': 11,
    'maverick': 12,
    'fabio': 20,
    'franco': 21,
    'enea': 23,
    'raul': 25,
    }

print("MotoGP Riders and there racing numbers.")

for key, value in favorite_numbers.items():
    print(f"The rider {key.title()}'s favorite number is {value}") 
