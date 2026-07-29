import pandas as pd

squirrel_data = pd.read_csv("./day25/squirrel project/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_colors = squirrel_data["Primary Fur Color"].to_list()

gray = squirrel_colors.count('Gray')
red = squirrel_colors.count('Red')
black = squirrel_colors.count('Black')
cinnamon = squirrel_colors.count('Cinnamon')

print("Gray: ", gray)
print("Red: ", red)
print("Black: ", black)
print("Cinnamon: ", cinnamon)

colors_dictionary = {
    "Colors": ['Gray', 'Red', 'Black', 'Cinnamon'],
    "Count": [gray, red, black, cinnamon] 
}

count_data = pd.DataFrame(colors_dictionary)
count_data.to_csv("./day25/squirrel project/count_data.csv")