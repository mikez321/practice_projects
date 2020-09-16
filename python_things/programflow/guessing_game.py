"""A number guessing game."""
from random import randint

answer = randint(1, 10)
guess = None

while answer != guess:
    print("Guess a number between 1 and 10!")
    guess = int(input())
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")

print("You got it, the number was {0}!".format(answer))
