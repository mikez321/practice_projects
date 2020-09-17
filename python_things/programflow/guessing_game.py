"""A number guessing game."""
from random import randint

top = 25
answer = randint(1, top)
guess = None

print(f"Guess a number between 1 and {top}!")
while answer != guess:
    guess = int(input())
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")

print("You got it, the number was {0}!".format(answer))
