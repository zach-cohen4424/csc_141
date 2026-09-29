# Zach is back at it. Absolutely killing Python, I might have to fight the cobra. Tests for equality and inequality with strings
name = "Zach"

print("Is name == 'Zach'? I predict True.")
print(name == "Zach")

print("\nIs name != 'Zach'? I predict False.")
print(name != "Zach")

# Tests using the lower() method
print("\nIs name.lower() == 'zach'? I predict True.")
print(name.lower() == "zach")

print("\nIs name.lower() == 'Zach'? I predict False.")
print(name.lower() == "Zach")

#Numerical tests
age = 18

print("\nIs age == 18? I predict True.")
print(age == 18)

print("\nIs age != 18? I predict False.")
print(age != 18)

print("\nIs age > 16? I predict True.")
print(age > 16)

print("\nIs age < 16? I predict False.")
print(age < 16)

print("\nIs age >= 18? I predict True.")
print(age >= 18)

print("\nIs age <= 16? I predict False.")
print(age <= 16)

# Tests using the and keyword
print("\nIs age > 16 and age < 20? I predict True.")
print(age > 16 and age < 20)

print("\nIs age > 20 and age < 25? I predict False.")
print(age > 20 and age < 25)

# Tests using the or keyword
print("\nIs age == 18 or age == 21? I predict True.")
print(age == 18 or age == 21)

print("\nIs age == 15 or age == 16? I predict False.")
print(age == 15 or age == 16)

# Test whether an item is in a list
favorite_sports = ["baseball", "football", "basketball"]

print("\nIs baseball in my favorite sports? I predict True.")
print("baseball" in favorite_sports)

print("\nIs soccer in my favorite sports? I predict False.")
print("soccer" in favorite_sports)

# Test whether an item is not in a list
print("\nIs soccer not in my favorite sports? I predict True.")
print("soccer" not in favorite_sports)

print("\nIs baseball not in my favorite sports? I predict False.")
print("baseball" not in favorite_sports)