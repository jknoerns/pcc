from pprint import pprint

favorite_language = "  Python  "

# display with tailing whitespace
print('String with whitespace')
pprint(favorite_language)

# display with trailing whitespace removed
print('\nString with right whitespace removed | rstrip()')
pprint(favorite_language.rstrip())

# display with leading whitespace removed
print('\nString with left whitespace removed | lstrip()')
pprint(favorite_language.lstrip())

# display with all whitespace removed
print('\nSring with all whitespace removed | strip()')
pprint(favorite_language.strip())

# removing prefixes
nostarch_url = "https://nostarch.com/"

# original url
print('\nURL as a string')
pprint(nostarch_url)

# remove the https:// prefix
print('\nURL with prefix removed | removeprefix("https://")')
pprint(nostarch_url.removeprefix("https://"))

# removing suffixes
filename = 'python_notes.txt'

# original filename
print('\nfilename as a srting')
pprint(filename)

# remove the .txt suffix
print('\nfilename with extension removed | removesuffix(".txt")')
pprint(filename.removesuffix(".txt"))
