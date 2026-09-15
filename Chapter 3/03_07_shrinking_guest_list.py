guests = ["Ray Lewis", "Ed Reed", "Ray Rice", "Jamal Lewis", "Terrell Suggs"]
guests.insert(0, "Joe Flacco")
guests.insert(2, "Kyle Hamilton")
guests.append("Derrick Henry")

print("Good news -- I found a bigger table!")
print("\nHere is the new set of invitations:")
for guest in guests:
    print(f"{guest}, I would love to have you over for dinner at my big house.")

    # Unfortunately, the bigger table won't arrive in time.
print("\nUnfortunately, I can only invite two people to dinner.")

# Remove guests one at a time from the end of the list until only
# two names remain, apologizing to each person as they're removed.
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Let the last two guests know they're still invited.
print(f"\n{guests[0]}, you're still invited to dinner.")
print(f"{guests[1]}, you're still invited to dinner.")

# Remove the last two names using del, leaving an empty list.
del guests[1]
del guests[0]

# Print the list to confirm it's empty.
print(f"\nRemaining guests: {guests}")
