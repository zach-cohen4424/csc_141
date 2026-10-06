# Doing more storing but of multiple favorite numbers for each person and then printing each person's name and their numbers.

favorite_numbers = {
    "Zach": [7, 12, 21],
    "Erik": [10, 15],
    "Ryan": [3, 8, 24],
    "James": [5, 11],
    "Coby": [4, 16]
}

for person, numbers in favorite_numbers.items():
    print("\n" + person + "'s favorite numbers are:")
    for number in numbers:
        print(number)