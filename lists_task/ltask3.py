list_1 = list(range(1, 101))
list_2 = []
counter = 0
while counter < len(list_1):
    if list_1[counter] % 7 == 0 and list_1[counter] % 5 != 0:
        list_2.append(list_1[counter])
    counter += 1
print(list_2)
