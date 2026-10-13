# tuples are terrific!
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

print("\nTry changing a value")
#dimensions[0] = 250
print("Commented that out to avoid an error.")

print("\nLooping over a tuple")
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

print("\nSo a tuple is immutable, but you can assign a new tuple to the variable:")
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
