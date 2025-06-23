capitals = {
    "France":"Paris",
    "Germany":"Berlin"
}

# travel_log = {
#     "France":["Paris", "Lille", "Dijon"],
#     "Germany":["Stuttgart", "Berlin"]
# }
#
# print(travel_log["France"][1])
# nested_list = ['A', 'B', ['C', 'D']]
#
# print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visited": ["Paris", "Lille", "Dijon"],
        "total_visits" : 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hanburg", "Stuttgart"],
        "total_visits": 5
    }
}

print(travel_log["Germany"]["cities_visited"][2])

# programming_dictionary = {
#     "bug":"An error in a program that causes it to run unexpectedly",
#     "function":"a piece of code to call over and over again"
#
# }

# print(programming_dictionary["bug"])
#
# programming_dictionary["loop"] = "action of coding over and over "
# print(programming_dictionary)
# #
# empty_dictionary = {}
# programming_dictionary = {}
# print(programming_dictionary)
#
# programming_dictionary["bug"] = "godrick narman"
# print(programming_dictionary)
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])