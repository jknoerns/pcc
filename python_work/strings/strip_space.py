from pprint import pprint

favorite_language = "  Python  "

# display with tailing whitespace
pprint(favorite_language)

# display with trailing whitespace removed
pprint(favorite_language.rstrip())

# display with leading whitespace removed
pprint(favorite_language.lstrip())

# display with all whitespace removed
pprint(favorite_language.strip())

# removing prefixes
nostarch_url = "https://nostarch.com/"

# original url
pprint(nostarch_url)

# remove the https:// prefix
pprint(nostarch_url.removeprefix("https://"))