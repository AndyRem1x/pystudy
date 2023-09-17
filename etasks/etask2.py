def count():
    try:
        a = int(input("Input first number:  "))
        b = int(input("Input second number:  "))
    except ValueError:
        return "Input values are not numbers"
    try:
        return a**2 / b
    except ZeroDivisionError:
        return "Cannot divide by zero"


print(count())
