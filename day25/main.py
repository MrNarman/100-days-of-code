# with open("./day25/weather_data - Sheet1.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


# import csv

# with open("./day25/weather_data - Sheet1.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas 

# data = pandas.read_csv("./day25/weather_data - Sheet1.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dictionary = data.to_dict()
# print(data_dictionary)

# temp_list = data["temp"].to_list()
# # average = sum(temp_list)/len(temp_list)
# # print(average)

# print( data["temp"].mean())
# print( data["temp"].max())
# print(data["condition"]) 

# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp *9/5 +32

# print(monday_temp_F)

#Create data frame from scratch
data_dict = {
    "students": ["Any", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("./day25/new_data.csv")