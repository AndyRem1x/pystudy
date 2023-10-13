from random import randint
list_1 = []
list_2 = []
length = 10
counter_1 = 0
counter_2 = 0
while counter_1 < length:
    list_1.append(randint(1, 10))
    counter_1 += 1
while counter_2 < length:
    list_2.append(randint(1, 10))
    counter_2 += 1
list_3 = [item for item in list_1 if item in list_2]
print(list(set(list_3)))
