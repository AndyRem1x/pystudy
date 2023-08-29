from random import randint, choice
a = randint(1, 20)
b = randint(1, 20)
operators = ["+", "-", "*", "/", "**", "//", "%"]
answer = 0
selected = choice(operators)
guess = input("If the answer of expression is decimal,"
              " round the number to two decimal places!"
              f"\n{a} {selected} {b} equals?: ")
if selected == "+":
    answer = a + b
elif selected == "-":
    answer = a - b
elif selected == "*":
    answer = a * b
elif selected == "/":
    answer = a / b
elif selected == "**":
    answer = a ** b
elif selected == "//":
    answer = a // b
elif selected == "%":
    answer = a % b
if float(guess) == round(float(answer), 2):
    print("You are right!")
else:
    print("You are wrong!")
