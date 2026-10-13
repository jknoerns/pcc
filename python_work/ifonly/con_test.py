car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'audi'? I predict False.")
print(car == 'audi')

print("\nTesting Conditions")
print("Set a rider variable equal to 'martin'")
rider = 'martin'
print("Set a team variable equal to 'aprillia'")
team = 'aprillia'
print(f"rider: {rider}, team: {team}")

print("\nTest the rider and the team, should be True.")
print(rider == 'martin' and team == 'aprillia')
print("\nTest the rider and the team where team is 'ducati', should be False.")
print(rider == 'martin'and team == 'ducati')
print("\nTest the rider or the team where team is 'ducati', should be True.")
print(rider == 'martin' or team == 'ducati')
print("\nTest the rider or the team where the rider is 'acosta', should be True.")
print(rider == 'acosta' or team == 'aprillia')
print("\nTest the rider or the team where the rider is 'acosta' and the team is 'ducati', should be False.")
print(rider == 'acosta' or team == 'ducati' )
