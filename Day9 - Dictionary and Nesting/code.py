#dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from rnning as expected",
    "Function": "A piece of code that you can easily call over and over again",
    "Loop": "The action of doing something over and over again",
}

#printing a dictionary
print(programming_dictionary)
print(programming_dictionary["Bug"])

#changing value
programming_dictionary["Loop"] = "This is changed"
print(programming_dictionary)

#creating an empty dictionary
empty_dictionary = {}

#wipe an entire dict
# programming_dictionary = {}
# print(programming_dictionary)

#loop in dict
for var in programming_dictionary:
    # print(f"{var}: {value}")
    print(var)
    print(programming_dictionary[var])

#nesting
#nested list
travel_log = {
    "France": ['Paris', 'Lille', 'Dijon'],
    "Germany": ['Stuttgart', 'Berlin'],
}

#printing
for country in travel_log:
    print(country, end=": ")
    for city in travel_log[country]:
        print(city, end=", ")
    print()

print(travel_log["France"][0])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

for list in nested_list:
    for li in list:
        print(li)

travel_log = {
    "France": {
        "cities_visited": ['Paris', 'Lille', 'Dijon'],
        "total_visit": 12
    },

    "Germany": {
        "cities_visited": ['Stuttgart', 'Berlin'],
        "total_visit": 13
    },
}

#printing weird structured dict
print(travel_log["Germany"]["cities_visited"][1])

for country in travel_log:
    print(country)
    print("the city list: ", end="")
    for city in travel_log[country]["cities_visited"]:
        print(city, end=", ")
    print("\nnumber of times visited: ", travel_log[country]["total_visit"])