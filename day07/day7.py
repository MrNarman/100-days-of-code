import random

word_list = ["baboon", "camel", "bananas", "government", "president", "america"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

# TODO-1 : using a while loop let the user guess again and again

guess = input("Guess a letter: ").lower()

display = ''

# TODO-2 : Change the for loop so that you keep the previous correct letter

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)




