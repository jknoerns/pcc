# make a list of cubes (**3) from 1 to 10
cubes = []
for value in range(1, 10):
    cube = value ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)

print()
# now with list comprehension
cubes = [value**3 for value in range(1, 10)]
for cube in cubes:
    print(cube)
