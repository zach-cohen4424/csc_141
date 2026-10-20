# Pizza Toppings 
# Zach Cohen
# Difficulty 3/10

pizzas = True 
while pizzas:
    toppings = input('Plain Cheese')
    if toppings == 'quit':
        pizzas = False 
        break
    else:
        print (f'We will add {toppings} to your pizza.')