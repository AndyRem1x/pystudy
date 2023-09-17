from random import randint
from module1 import generate_question

username = input("Please input your name: ")
print(generate_question(username))
user_guess = input()


def check_guess(user_guess):
    guess = randint(1, 20)
    if int(user_guess) == guess:
        return "You guessed the number!"
    else:
        return "You didn't guess the number!"


print(check_guess(user_guess))
