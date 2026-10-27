favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n\n")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\nAll the names (keys).")
for name in favorite_languages.keys():
    print(name)

print("\nAll the names (keys) again, as it's the default.")
for name in favorite_languages:
    print(name)

print("\nHighlight my friends.")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")

print("\nTime to sort the names (keys).")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
