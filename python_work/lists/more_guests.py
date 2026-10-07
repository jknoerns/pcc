# invite some guests to dinner
guest_list = ['Valentino Rossi','Fabio Quartararo','Toprak Razgatlioglu','Jack Miller']

print(f"Hello Mr. {guest_list[0]}, would you like to go to dinner?")
print(f"Hello Mr. {guest_list[1]}, would you like to go to dinner?")
print(f"Hello Mr. {guest_list[2]}, would you like to go to dinner?")
print(f"Hello Mr. {guest_list[3]}, would you like to go to dinner?")

# ut oh, Valentino cannot make it
print("\nUnfortunately Vale cannot make it!")
# invite another guest
print("\nInviting Pedro!")
guest_list[0] = 'Pedro Acosta'

print(f"\nHello Mr. {guest_list[0]}, would you like to go to dinner?")
print(f"Hello Mr. {guest_list[1]}, would you like to go to dinner?")
print(f"Hello Mr. {guest_list[2]}, would you like to go to dinner?")
print(f"Hello Mr. {guest_list[3]}, would you like to go to dinner?")

print(f"\nHello {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, and {guest_list[3]}.")
print("We have a larger table, so I will invite more guests.")

# adding Marco Bezzecchi to the beginning of the list
print("\nAdding Marco Bezzecchi to the beginning of the guest list. | .insert(0, 'Marco Bezzecchi')")
guest_list.insert(0, 'Marco Bezzecchi')
# adding Jorge Martin to the middle of the list
print("Adding Jorge Martin to the middle of the guest list. | .insert(2, 'Jorge Martin'")
guest_list.insert(2, 'Jorge Martin')
# adding Brad Binder to the end of the list
print("Adding Brad Binder to the end of the guest list. | .append('Brad Binder')")
guest_list.append('Brad Binder')

# print the new invitations
print(f"\nHello Mr. {guest_list[0]}, please join us for a fabulous dinner.")
print(f"Hello Mr. {guest_list[1]}, please join us for a fabulous dinner.")
print(f"Hello Mr. {guest_list[2]}, please join us for a fabulous dinner.")
print(f"Hello Mr. {guest_list[3]}, please join us for a fabulous dinner.")
print(f"Hello Mr. {guest_list[4]}, please join us for a fabulous dinner.")
print(f"Hello Mr. {guest_list[5]}, please join us for a fabulous dinner.")
print(f"Hello Mr. {guest_list[6]}, please join us for a fabulous dinner.")
