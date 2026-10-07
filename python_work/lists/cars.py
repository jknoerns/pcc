# list of car manufacturers
cars = ['honda','bmw','chevrolet','ford','audi','mercedes','mazda']

# permenant sort
print(f"Original list of car manufacturers: {cars}")
print("sorting...| .sort()")
cars.sort()
print(f"New sorted list of car manufacturers: {cars}")

# permenant sort in reverse order
print("\nLet's reverse the list")
print("sorting...| .sort(reverse=True)")
cars.sort(reverse=True)
print(f"New reverse sorted list of car manufacturers: {cars}")

# sort without changing the originall order
cars = ['honda','bmw','chevrolet','ford','audi','mercedes','mazda']
print(f"\nOkay, back to the original, unsorted list: {cars}")
print("Time for a temporary sort...| sorted(cars)")
print(f"\nHere is the original list: {cars}")
print(f"\nHere is the sorted list: {sorted(cars)}")
print(f"\nHere is the original list again: {cars}")

# reverse order but not sorted
print("\nWhat if we just reverse the list order?")
print(f"Here is the list: {cars}")
cars.reverse()
print(f"And here it is reversed: {cars}")

# length of the list
print(f"The lenght of the list named cars is: {len(cars)}")
