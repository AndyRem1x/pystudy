import random
string = input("Input some string:  ")
lst = list(string)
for i in range(5):
    j = 0
    nstring = ''
    random.shuffle(lst)
    while j < len(lst):
        nstring += lst[j]
        j += 1
    print(nstring)
