guests = ["Ray Lewis", "Ed Reed", "Ray Rice", "Jamal Lewis", "Terrell Suggs"]
print(f"{guests[0]} I would love to have you over for dinner at my big house.")
print(f"{guests[1]} I would love to have you over for dinner at my big house.")
print(f"{guests[2]} I would love to have you over for dinner at my big house.")
print(f"{guests[3]} I would love to have you over for dinner at my big house.")
print(f"{guests[4]} I would love to have you over for dinner at my big house.")

# Jamal Lewis can't make it to dinner, so let's replace him with another guest. 
print(f"\n{guests[3]} can't make it to dinner.")

# Replace him with another guest, "Lamar Jackson"
guests[3] = "Lamar Jackson"

# Send a new set of invitations to everyone still on the list. 
print("\nHere is the new set of invitations:")
print(f"{guests[0]} I would love to have you over for dinner at my big house.")
print(f"{guests[1]} I would love to have you over for dinner at my big house.")
print(f"{guests[2]} I would love to have you over for dinner at my big house.")
print(f"{guests[3]} I would love to have you over for dinner at my big house.")
print(f"{guests[4]} I would love to have you over for dinner at my big house.")
