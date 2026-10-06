# More storing of information but this time about three cities, including their country, population, and a fact about each city.
# One more to go, consistent python power. 
cities = {
    "Baltimore": {
        "country": "United States",
        "population": "Around 565,000",
        "fact": "It is known for its Inner Harbor."
    },

    "Philadelphia": {
        "country": "United States",
        "population": "Around 1.6 million",
        "fact": "The Liberty Bell is located there."
    },

    "New York City": {
        "country": "United States",
        "population": "Around 8 million",
        "fact": "It is home to Times Square."
    }
}

for city, information in cities.items():
    print("\n" + city + ":")
    for key, value in information.items():
        print(key.title() + ": " + value)