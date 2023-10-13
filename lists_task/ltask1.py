from random import randint
lst = []
length = 10
counter = 0
while counter < length:
    lst.append(randint(1, 20))
    counter += 1
print(max(lst))
