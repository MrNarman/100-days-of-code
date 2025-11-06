from art import logo
from art import vs
from game_data import data
from random import randint


# todo: print art and the comparison statements | Include also the score

user_score = 0
detail_index_A = randint(0, 49)
detail_index_B = randint(0, 49)
def main_game_structure(score):
    print(f"{logo}\nyour score is: {score}")
    get_data_A(detail_index_A)
    print(vs)
    get_data_B(detail_index_B)


# todo: get data from game_data file to form the questions
def get_data_A(index):
    """
        Gets data for statement A to be used for comparison.
    """
    print(f"Compare A: {data[index]['name']},a {data[index]['description']}, from {data[index]['country']} ")
def get_data_B(index):
    """
        Gets data for statement B to be used for comparison.
    """
    print(f"Against B: {data[index]['name']},a {data[index]['description']}, from {data[index]['country']} ")

# Call the function of the game
main_game_structure(user_score)

# todo: get comparisons for statements A and B
user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

# todo: Switch statement B to A incase user is correct
# todo: stop the game when the user fails and print out score


