# I am doing more of storing people's favorite places in a dictionary and then printing each person's name and their favorite places.

favorite_places = {
    "Zach": ["Ocean City", "Baltimore", "New York"],
    "Erik": ["Florida", "Virginia"],
    "Ryan": ["California", "Maine", "Hawaii"]
}

for person, places in favorite_places.items():
    print("\n" + person + "'s favorite places are:")
    for place in places:
        print("- " + place)