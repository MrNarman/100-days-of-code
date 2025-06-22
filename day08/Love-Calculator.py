# def calculate_love_score(name1, name2):
#     list1 = ['T', 'R', 'U', 'E']
#     list2 = ['L', 'O', 'V', 'E']
#     count1= 0
#     count2= 0
#     for char in name1:
#         if char in list1:
#             count1+=1
#
#     for char in name2:
#         if char in list2:
#             count2+=1
#     print(f"Love score = {count1}{count2}")
#
# calculate_love_score("KANYE WEST", "KIM KARDASHIAN")

def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)

calculate_love_score("Kanye West", "Kim Kardashian")