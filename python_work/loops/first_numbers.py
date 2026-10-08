# using range

# stops when it reaches 5, output is 1 to 4
print("Output of for loop with range(1, 5)")
for value in range(1, 5):
    print(value)

# can also exclude the starting value, default starts at zero
print("\nOutput of for loop with range(6)")
for num in range(6):
    print(num)

# assign a range to a variable
print("\nNo loop, just assigning a range to a var.")
numbers = list(range(1, 6))
print(numbers)

# range can even skip numbers
print("\nOnly even numbers range(2, 11, 2)")
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# can create almost any set of numbers, like squares
print("\nSquare numbers from range(1, 11)")
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
