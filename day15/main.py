MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

QUARTERS = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

# todo: print report
def get_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")

# todo: process coins
def process_coins(qtrs, dme, nckl, pnny):
    total_value = (QUARTERS*qtrs) + (DIME*dme) + (NICKEL*nckl) + (PENNY*pnny)
    return total_value

def make_espresso(resources_water, resources_coffee):
    """Calculates the resources to be deducted when making an espresso"""
    espresso_water = MENU['espresso']['ingredients']['water']
    espresso_coffee = MENU['espresso']['ingredients']['coffee']

    if resources_water < espresso_water:
        print("Not enough water to make an espresso!")
    elif resources_coffee < espresso_coffee:
        print("Not enough coffee to make and espresso!")
    else:
        resources['water'] = resources_water - espresso_water
        resources['coffee'] = resources_coffee - espresso_coffee
        print("Here is your espresso ☕️. Enjoy!")


make_coffee = True
while make_coffee:
    # todo: Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
    user_coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TEST ENVIRONMENT- TO BE DELETED
    make_espresso(resources['water'], resources['coffee'])
    # END OF TEST ENVIRONMENT

    # print("Please insert coins.")
    # user_quarters = int(input("How many quarters : "))
    # user_dimes = int(input("How many dimes : "))
    # user_nickels = int(input("How many nickels : "))
    # user_pennies = int(input("How many pennies : "))
    #
    # print(process_coins(user_quarters, user_dimes, user_nickels, user_pennies))
    #
    # todo: Turn off the Coffee Machine by entering 'off' to the prompt
    if user_coffee_choice == 'off':
        make_coffee = False
    elif user_coffee_choice == 'report':
        get_report()

# todo: check resources sufficient
# todo: check transaction successful
# todo: make coffee and deduct the resources
