places = ["Bahamas", "Rome", "Sicily", "Puerto Rico", "Shri Lanka"]

# Print the list in its original order.
print(places)

# Use sorted() to print the list alphabetically without changing it.
print(sorted(places))

# Show the list is still in its original order.
print(places)

# Use sorted() to print the list in reverse alphabetical order,
# again without changing the original list.
print(sorted(places, reverse=True))

# Show the list is still in its original order.
print(places)

# Use reverse() to change the order of the list, then print it.
places.reverse()
print(places)

# Use reverse() again to put the list back in its original order.
places.reverse()
print(places)

# Use sort() to permanently sort the list alphabetically.
places.sort()
print(places)

# Use sort() to permanently sort the list in reverse alphabetical order.
places.sort(reverse=True)
print(places)
