from random import randint
a = randint(1, 20)
b = randint(1, 20)
answer = input(f"{a} + {b} equals? ")
if int(answer) == (a + b):
    print("You are right!")
else:
    print("You are wrong!")
