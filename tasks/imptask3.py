import random
string = input("Input some string:  ")
lst = list(string)
for i in range(5):
    j = 0
    new_string = ''
    random.shuffle(lst)
    while j < len(lst):
        new_string += lst[j]
        j += 1
    print(new_string)
