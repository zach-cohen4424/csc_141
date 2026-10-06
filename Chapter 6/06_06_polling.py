# I am creating a list of my friends to see who have already taken a favorite programming language poll. If they didn't say Python then we are no longer friends. They have to feel the power of python. 

favorite_languages = {
    "erik": "python",
    "ryan": "c",
    "james": "ruby",
    "coby": "python"
}

people_to_poll = ["erik", "ryan", "james", "coby", "nick", "mason"]

for person in people_to_poll:
    if person in favorite_languages:
        print("Thank you, " + person.title() + ", for taking the poll!")
    else:
        print(person.title() + ", please take our favorite languages poll.")

