# I created more dictionaries for different pets and store the type of animal and the owner's name.

pet1 = {
    "animal": "dog",
    "owner": "Erik"
}

pet2 = {
    "animal": "cat",
    "owner": "Ryan"
}

pet3 = {
    "animal": "fish",
    "owner": "James"
}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("\nPet:")
    for key, value in pet.items():
        print(key.title() + ": " + value.title())