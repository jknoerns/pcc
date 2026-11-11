# is it a multiple of ten
by_ten = input("Please enter a number and I will check if it is a multiple of ten. ")
by_ten = int(by_ten)

if by_ten % 10 == 0:
    print(f"\nYes, your number {by_ten} is a multiple of ten!")
else:
    print(f"Oh no, your number {by_ten} is not a multiple of ten.")
