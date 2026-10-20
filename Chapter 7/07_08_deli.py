# in the deli
# deli life 
# Zach Cohen
# Difficulty: 3/10

sandwich_orders = ['pastrami', 'ham', 'turkey', 'salami']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made your {sandwich} sandwich.')
    finished_sandwiches.append(sandwich)

print('\nThe following sandwiches were made:')
for sandwich in finished_sandwiches:
    print(sandwich)