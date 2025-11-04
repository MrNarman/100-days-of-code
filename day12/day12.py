from random import randint
from logo import art

print(art)
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
random_number_CPU = randint(1, 100)

attempts = 0
difficulty = input("Choose your difficulty, 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    attempts = 10
else:
    attempts = 5

while attempts > 0:
    random_number_USER = int(input(f"You have {attempts} attempts remaining. \nMake a guess: "))

    if random_number_USER > random_number_CPU:
        print("TOO HIGH!")
    elif random_number_USER < random_number_CPU:
        print("TOO LOW!")

    if random_number_USER == random_number_CPU:
        print(f"Hurray!\n You got it. The number is {random_number_CPU}")
        break

    attempts -= 1
    if attempts == 0:
        print(f"\nYou ran out of attempts and failed to guess the number.\nThe number is {random_number_CPU}")
        break
