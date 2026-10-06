# I got information about three different people into dictionaries and then puts the dictionaries into a list.

person1 = {
    "first_name": "Zach",
    "last_name": "Cohen",
    "age": 18,
    "city": "Timonium"
}

person2 = {
    "first_name": "Erik",
    "last_name": "Smith",
    "age": 18,
    "city": "Baltimore"
}

person3 = {
    "first_name": "Ryan",
    "last_name": "Jones",
    "age": 19,
    "city": "Philadelphia"
}

people = [person1, person2, person3]

for person in people:
    print("\nPerson:")
    for key, value in person.items():
        print(key.title() + ": " + str(value))