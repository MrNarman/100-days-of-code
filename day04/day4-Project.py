# ROCK PAPER SCISSORS
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gestures = [rock, paper, scissors]

computer_choice = random.randint(0, 2)
user_choice = int(input("What do you choose? 0 for ROCK, 1 for PAPER, 2 for SCISSORS: "))
if user_choice == computer_choice:
    print(f"you picked \n {gestures[user_choice]}" + f"\n Computer picked {gestures[computer_choice]}")
    print("It's a draw")

elif user_choice == 0 and computer_choice == 1:
    print(f"you picked \n {gestures[user_choice]}" + f"\n Computer picked {gestures[computer_choice]}")
    print("You lost! PAPER beats ROCK")

elif user_choice == 0 and computer_choice == 2:
    print(f"you picked \n {gestures[user_choice]}" + f"\n Computer picked {gestures[computer_choice]}")
    print("You win. ROCK beats SCISSORS")

elif user_choice == 1 and computer_choice == 0:
    print(f"you picked \n {gestures[user_choice]}" + f"\n Computer picked {gestures[computer_choice]}")
    print("You win! PAPER beats ROCK")

elif user_choice == 1 and computer_choice == 2:
    print(f"you picked \n {gestures[user_choice]}" + f"\n Computer picked {gestures[computer_choice]}")
    print("You lost! SCISSORS beats PAPER")

elif user_choice == 2 and computer_choice == 0:
    print(f"you picked \n {gestures[user_choice]}" + f"\n Computer picked {gestures[computer_choice]}")
    print("You lost! ROCK beats SCISSORS")

elif user_choice == 2 and computer_choice == 1:
    print(f"you picked \n {gestures[user_choice]}" + f"\n Computer picked {gestures[computer_choice]}")
    print("You win! SCISSORS beats PAPER")

else:
    print("Invalid input")
