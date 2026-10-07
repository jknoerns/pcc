# list of motorcycles
motorcycles = ['honda','kawasaki','yamaha','ducati']

# a note about Honda
print(f"I did not own a {motorcycles[0].title()}, but I raced one!")

# a note about Kawasaki
print(f"\nI owned several motorcycles from {motorcycles[1].title()}.")

# something about Yamaha
print(f"\nI never owned a {motorcycles[2].title()}.")

# and now Ducati
print(f"\nI love {motorcycles[-1].title()} motorcycles, but have not owned one yet.")

print(f"\nThe original third item is {motorcycles[2]}.")
# change an element of the list
motorcycles[2] = 'KTM'

print(f"\n\tThe new third item is {motorcycles[2]}.")

# adding elements to the end of a list with append
print("\nAdding Suzuki to the motorcycles list...")
print(f"Original list {motorcycles}")
motorcycles.append('suzuki')
print(f"List with new element at the end {motorcycles}.")

# create a new list with append starting with an empty list
lesser_bikes = []
print(f"\nNew list with no elements {lesser_bikes}.")
print("Appending cagiva.")
lesser_bikes.append('cagiva')
print(f"\nNew list with one element {lesser_bikes}.")
print("Appending can am.")
lesser_bikes.append('can am')
print(f"\nNew list with two elements {lesser_bikes}.")
print("Appending bsa")
lesser_bikes.append('bsa')
print(f"\nNew list with three elements {lesser_bikes}.")

# insert element into a list using insert
print(f"\nCurrent list {lesser_bikes}")
print("Inserting 'indian' as the second element with insert.")
lesser_bikes.insert(1, 'indian')
print(f"Now the list looks like this {lesser_bikes}")


# remove elements from a list using del
print(f"\nCurrent list {lesser_bikes}")
print("Removing the third element from the list with del.")
del lesser_bikes[2]
print(f"Now the list looks like this {lesser_bikes}")

# remove an element from a list with pop, so the element can be used
print("\nAdding two more motorcycles to the list.")
lesser_bikes.append('jawa')
lesser_bikes.append('lightning')
print(f"Current list {lesser_bikes}")
print("Without parameters, pop removes the last element.")
popped_bike = lesser_bikes.pop()
print(f"Now the list looks like this {lesser_bikes}")
print(f"And the motorcycle that was removed is {popped_bike}.")

# remove the second list item with pop
print(f"\nCurrent list {lesser_bikes}")
print("Poping the second item with pop | pop(1)")
popped_item2 = lesser_bikes.pop(1)
print(f"Now the list looks like this {lesser_bikes}")
print(f"And the motorcycle that was removed is {popped_item2}.")

# remove an element by value
print(f"\nCurrent list {lesser_bikes}")
print("Using remove to elimnate 'jawa' from the list | .remove('jawa')")
lesser_bikes.remove('jawa')
print(f"Now the list looks like this {lesser_bikes}")
