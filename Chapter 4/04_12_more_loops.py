my_foods = ["pizza", "rice", "chicken"]
friend_foods = my_foods[:]
friend_foods.append("pasta")

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("My friend's favorite foods are:")
for food in friend_foods:
    print(food)