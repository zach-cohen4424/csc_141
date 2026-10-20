# Dream vacation spot
# Zach Cohen
# Difficulty: 4/10

responses = {}

polling = True
while polling:
    name = input('What is your name? ')
    vacation = input('If you could visit one place in the world, '
                     'where would you go? ')

    responses[name] = vacation

    repeat = input('Would someone else like to answer? (yes/no) ')

    if repeat == 'no':
        polling = False

print('\n--- Dream Vacation Results ---')

for name, vacation in responses.items():
    print(f'{name} would like to visit {vacation}.')