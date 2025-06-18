import random

stages = [r''' 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["baboon", "camel", "bananas", "government", "president", "america"]

# TODO-1 : Create a variable called lives to keep track of the number of lives left.
#  Set 'lives' to equal 6
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    # TODO-2 : if guess is not in the chosen_word, then reduce lives by 1.
    #  If lives goes down to 0 then the game should end, and it should print "You loose"
    if guess not in chosen_word:
        lives -= 1
    elif lives == 0:
        game_over = True
        print("You loose")

    if "_" not in display:
        game_over = True
        print("You win")

    # TODO-3 : Print the ASCII art from 'Stages'
    #  that corresponds to the current number of 'lives' the user has remaining

    print(stages[lives])




