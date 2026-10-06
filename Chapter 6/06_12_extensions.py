# I'm going to expland the favorite numbers program by adding the person's favorite sport along with their favorite numbers.
# Full python power achived

favorite_information = {
    "Zach": {
        "numbers": [7, 12, 21],
        "sport": "baseball"
    },

    "Erik": {
        "numbers": [10, 15],
        "sport": "football"
    },

    "Ryan": {
        "numbers": [3, 8, 24],
        "sport": "basketball"
    }
}

for person, information in favorite_information.items():
    print("\n" + person + ":")
    print("Favorite numbers:", information["numbers"])
    print("Favorite sport:", information["sport"])