string = input("Input your string: ")
if len(string) >= 2:
    print(string[0:2] + string[-2:])
else:
    print("Empty string")
