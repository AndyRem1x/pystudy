from random import randint
number = randint(1, 10)
guess = int(input("Guess the number between 1 and 10:  "))
if guess == number:
    print("You guessed the number!")
else:
    print(f"You didn't guess the number! The right number is {number}.")
