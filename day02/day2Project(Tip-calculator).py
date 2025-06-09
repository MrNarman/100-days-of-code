print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, 15? "))
people_to_split = int(input("How many people to split the bill? "))

split_per_person = (total_bill * ((tip / 100) + 1)) / people_to_split

print(f"Each person should pay: {round(split_per_person, 2)}")
