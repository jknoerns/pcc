# loop over a list of types of pizza
# I prefer two boots, so some names will be uncommon

my_pizzas = ['V for Vegan','Earth Mother','The VCBGB', 'Vegan Cleo']
friends_pizzas = my_pizzas[:]

my_pizzas.append('Vegan Mr. Pink')
friends_pizzas.append('Super Vegan')

print("My favorite pizza's are:")
for pizza in my_pizzas:
    print(pizza)

print("\nMy friends favorite pizza's are:")
for pizza in friends_pizzas:
    print(pizza)
