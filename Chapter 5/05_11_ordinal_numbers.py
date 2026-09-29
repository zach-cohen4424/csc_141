#This code is pretty simple, first creating a range of numbers, then using a list to change endings of numbers. 
numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print("1st")

    elif number == 2:
                print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")

