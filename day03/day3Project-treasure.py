print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to treasure island")
print("Your mission iso find the treasure")

choice1 = input("You are at a crossroad, where do you want to go? left or right: " ).lower()

if choice1 == "left":
    choice2 = input("You have come to the island. The island is in the middle of the lake"
                    "type \'wait\' to wait and \'swim\' to swim: ").lower()
    if choice2 == "wait":
        choice3 = input("You are at an island unharmed. the house has 3 dyas"
                        "choose color of door youd like. Red, blue or yellow: ")

        if choice3 == "red":
            print("You were attacked by a bear. Game over")
        elif choice3 == "blue":
            print("You were bitten by a snake")
        elif choice3 == "yellow":
            print("Hurray. You found the treasure")
        else:
            print("Invalid choice.")

    else:
        print("You were attacked an animal")
else:
    print("You fell into a river! Game over")