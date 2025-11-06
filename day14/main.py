from art import logo
from art import vs
from game_data import data
from random import randint

user_score = 0
detail_index_A = randint(0, 49)
detail_index_B = randint(0, 49)
game_continue = True

# todo: print art and the comparison statements | Include also the score
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

# Function to get follower count from the provided index
def get_followers(index):
    follower_count = data[index]['follower_count']
    return follower_count

# main code
while game_continue:
    # Call the function of the game
    main_game_structure(user_score)

    # todo: get comparisons for statements A and B
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    def check_answer(user_input, followers_A, followers_B):
        if followers_A > followers_B:
            return user_input == 'a'
        else:
            return user_input == 'b'

    # todo: stop the game when the user fails and print out score
    if not check_answer(user_guess, get_followers(detail_index_A), get_followers(detail_index_B)):
        # Clear the screen after failure and print final score
        print("\n"*50 + logo)
        print(f"That's wrong. Your final score is {user_score}")
        break
    else:
        detail_index_A = detail_index_B
        if detail_index_A == detail_index_B:
            detail_index_B = randint(0, 49)

        user_score += 1
        print("\n" * 50)
        