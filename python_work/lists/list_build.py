# build a list using append, assignment, insert
# start with an empty list
parts = []

#append to the list
print("Start with an empty list...")
print(parts)

print("\nAppend 'wheels' to the list...")
parts.append('wheels')
print(parts)

print("\nAdd more parts...")
parts.append('brakes')
parts.append('forks')
print("Current list...")
print(parts)

print("\nChange the first item to 'tires'")
parts[0] = 'tires'
print(parts)

print("\nInsert 'engine' as the second item...")
parts.insert(1, 'engine')
print(parts)
