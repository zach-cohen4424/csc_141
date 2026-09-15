guests = ["Ray Lewis", "Ed Reed", "Ray Rice", "Jamal Lewis", "Terrell Suggs"]

# Announce the bigger table.
print("Good news -- I found a bigger table!")

# Add one new guest to the beginning of the list.
guests.insert(0, "Joe Flacco")

# Add one new guest to the middle of the list.
guests.insert(2, "Kyle Hamilton")

# Add one new guest to the end of the list.
guests.append("Derrick Henry")

# Print a new set of invitation messages for everyone in the list.
print("\nHere is the new set of invitations:")
for guest in guests:
    print(f"{guest}, I would love for you to join me for dinner.")