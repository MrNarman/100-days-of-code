# with open("trial.txt") as trial_file:
#     content =  trial_file.read()
#     print(content)

with open("trial.txt", "a") as file:
    file.write("\nWelcome to kenya")

with open("new_file.txt", "w") as wfile:
    wfile.write("banana")
    