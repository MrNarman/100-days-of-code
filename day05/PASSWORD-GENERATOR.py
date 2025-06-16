import random

# List of all letters (lowercase and uppercase)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# List of all numbers
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of all symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
           '+', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '?']

print("Welcome to the PyPassword Generator!")
user_letters = int(input("How many letters would you like in your password?\n"))
user_symbols = int(input("How many symbols would you like?\n"))
user_numbers = int(input("How many numbers would you like?\n"))

# EASY LEVEL
password = ''
for letter in range(user_letters):
    password += random.choice(letters)

for symbol in range(user_symbols):
    password += (random.choice(symbols))

for number in range(user_numbers):
    password += (random.choice(numbers))

print(password)


