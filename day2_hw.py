# Exercise 1:

places = [" ", "Argentina", " ", "San Diego",
          "", "  ", "", "Boston", "New York"]

res = []
for place in places:
    if place.strip() != '':
        res.append(place)
print(res)


#Exercise 2:
author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield",
    "David hassELHOFF", "Gary A.J. Bernstein"]


def SortFunct(name_list):
    name_list.sort(key=lambda name: name.title().split()[-1])
    return name_list


print(SortFunct(author))

# Exercise 3:

# F = (9/5)*C + 32
places = [('Nashua', 32), ("Boston", 12), ("Los Angelos", 44), ("Miami", 29)]

place_updated = list(map(lambda x: (x[0], ((x[-1]*1.8 + 32))), places))

print(place_updated)

# Exercise 4

def fibSeq(num):
    if num <= 1:
        return num
    else:
        return (fibSeq(num-2) + fibSeq(num-1))

n_terms = 6

if n_terms <= 0:
    print("Only Positive Number")
else:
    for i in range(0, n_terms):
        print(f"Iteration {i}:{fibSeq(i+1)}")
