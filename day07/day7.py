import random
from hangman_art import hangman_logo, stages
from hangman_words import word_list

lives = 6
print(hangman_logo)

chosen_word = random.choice(word_list)

placeholder = ""
for letter in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT**************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You loose a life")

        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word} YOU LOOSE*******************")

    if "_" not in display:
        game_over = True
        print("***********************YOU WIN**********************")

    print(stages[lives])




