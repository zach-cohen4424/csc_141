# Three exists 
#Zach Cohen
# Using a condition to stop the loop, using a active variable, and using a break statement. 
# Difficulty:4/10

number = 1

while number != 0:
    number = int(input('Enter a number (0 to quit): '))
    print (f'You entered {number}.')   

active = True

while active:
    number = input('Enter a number (or quit): ')
    if number == 'quit':
        active = False
    else:
        print(f'You entered {number}.')

while True:
    number = input('Enter a number (or quit): ')
    if number == 'quit':
        break
    else:
        print(f'You entered {number}.')