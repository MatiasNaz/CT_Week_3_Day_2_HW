# Exercise 1:

places = [" ", "Argentina", " ", "San Diego",
          "", "  ", "", "Boston", "New York"]


def VisitPlaces(filter(lambda place: place True if places.strip()[0]))


#Exercise 2:
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield",
    "David hassELHOFF", "Gary A.J. Bernstein"]


def SortFunct(name_list):
    name_list.sort(key=lambda name: name.title().split()[-1])
    return name_list


print(SortFunct(author))


#     #sort_list = sort(author.items(), key=lambda item: item[1])
#     print(sort_tuples) [(1,1), (3,4), (2,9)]

#     sort_list = {k: v for k, v in sort_tuples}

# print(sort_list)


# sorted_tuples = sorted(dict1.items(), key=lambda item: item[1])
# print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
# sorted_dict = {k: v for k, v in sorted_tuples}

# print(sorted_dict)  # {1: 1, 3: 4, 2: 9}


# Exercise 3:


# F = (9/5)*C + 32
places = [('Nashua', 32), ("Boston", 12), ("Los Angelos", 44), ("Miami", 29)]

# x = list(places)
# places = tuple(x)

# print(places)
places = list(map(lambda x: (x[0], ((x[-1])*1.8)+32, places))


              print(places)

# Exercise 4