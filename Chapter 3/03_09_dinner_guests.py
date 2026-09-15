guests = ["Ray Lewis", "Ed Reed", "Ray Rice", "Jamal Lewis", "Terrell Suggs"]
guests.insert(0, "Joe Flacco")
guests.insert(2, "Kyle Hamilton")
guests.append("Derrick Henry")

print("Here is the new set of invitations:")
for guest in guests:
    print(f"{guest}, I would love to have you over for dinner at my big house.")

    number_of_guests = len(guests)
print(f"\nI'm inviting {number_of_guests} people to dinner.")
