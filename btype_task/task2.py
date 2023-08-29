number = input("Input phone number: ")
if number.isdigit() and len(number) == 10:
    print("Phone number is valid")
else:
    print("Phone number is not valid")
