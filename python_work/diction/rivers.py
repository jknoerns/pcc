rivers = {
    'amazon': 'south america',
    'yangtze': 'asia',
    'mississippi': 'north america',
}

for river, country in rivers.items():
    print(f"The {river.title()} river is in {country.title()}")

print("\nWorld famous rivers!")
for river in rivers.keys():
    print(f"\t{river.title()}")

print("\nCountries with famous rivers!")
for country in rivers.values():
    print(f"\t{country.title()}")
