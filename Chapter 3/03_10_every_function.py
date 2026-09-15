beaches = ["Wildwood", "Ocean City", "Cape May", "Bethany"]

# Print the full list.
print(beaches)

# Print how many beaches are in the list.
print(f"Number of beaches: {len(beaches)}")

# Print the list in alphabetical order without changing it.
print(sorted(beaches))

# Print the list in reverse alphabetical order without changing it.
print(sorted(beaches, reverse=True))

# Confirm the original list order hasn't changed.
print(beaches)

# Add a new beach to the end of the list.
beaches.append("Rehoboth Beach")
print(beaches)

# Insert a new beach at the beginning of the list.
beaches.insert(0, "Dewey Beach")
print(beaches)

# Reverse the order of the list.
beaches.reverse()
print(beaches)

# Sort the list permanently in alphabetical order.
beaches.sort()
print(beaches)

# Remove and print the last beach in the list using pop().
last_beach = beaches.pop()
print(f"Removed with pop(): {last_beach}")
print(beaches)

# Remove the first beach in the list using del.
del beaches[0]
print(beaches)

# Loop through the remaining list and print each beach.
for beach in beaches:
    print(f"I would love to re-visit {beach} someday.")