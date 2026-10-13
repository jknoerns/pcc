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

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())
