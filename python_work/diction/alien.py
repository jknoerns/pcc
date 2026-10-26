alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"\nYou just earned {new_points} points!")

print("\nPrint out the dictionary alien_0")
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print("\nAdded new keys/values, now alien_0 looks like this.")
print(alien_0)

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5

print("\nCreated a new empty dictionary and added color and points.")
print(alien_1)

alien_2 = {'color': 'green'}
print(f"\nThe color of alien_2 is {alien_2['color']}")
alien_2['color'] = 'yellow'
print(f"\nCondition has changed, alien_2 is now {alien_2['color']}")

alien_3 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"\nOriginal position of alien_3: {alien_3['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_3['speed'] == 'slow':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien
    x_increment = 3

# The new postion is the old position plus the increment
alien_3['x_position'] = alien_3['x_position'] + x_increment

print(f"\nNew postion of alien_3: {alien_3['x_position']}")
