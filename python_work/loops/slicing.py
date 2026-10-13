players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("All Players")
print(players)

print("\nPlayers 0:3")
print(players[0:3])

print("\nPlayers 1:4")
print(players[1:4])

print("\nPlayers :4")
print(players[:4])

print("\nPlayers 2:")
print(players[2:])

print("\nPlayers -3:")
print(players[-3:])

# end of chapter exercises
print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())

print("\nThe first three items in the list are:")
print(players[:3])

print("\nThree items from the middle of the list are:")
print(players[1:4])

print("\nThe last three items in the list are:")
print(players[-3:])
