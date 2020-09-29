"""Improve playability of guessing game with function."""
from random import randint


def valid_input(prompt):
    """Return a valid number or loop if invalid input."""
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("That is not a valid number. Try again.")


top = 20
answer = randint(1, top)
guess = None

print(f"The answer is {answer}")
print(f"Please guess a number between 1 and {top}: ")
while answer != guess:
    guess = valid_input(": ")
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")

print("You got it, the number was {0}!".format(answer))
