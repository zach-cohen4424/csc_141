# Movie Tickets
# Zach Cohen
# Difficulty 3/10

tickets = True
while tickets:
    age_of_person = input('How old are you?: ')
    if age_of_person == 'quit':
        tickets = False
    elif int(age_of_person) < 3:
        print('You can watch the movie for free.')
    elif int(age_of_person) >=3 and int(age_of_person) <= 12:
        print('Your ticket price is $10.')
    else:
        print('Your ticket price is $15.')