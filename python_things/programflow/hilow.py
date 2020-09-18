"""Write a binary search algorithm."""

low = 1
high = 1000

print("Please think of a number between {0} and {1}".format(low, high))
input("Press ENTER to start")

count = 1

while low != high:
    guess = low + (high - low) // 2
    # the above formula was presented in the slides of the previous lesson
    # and calculates the midpoint of two numbers in a binary search
    # fashion.
    high_low = input("My guess is {}.  Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct."
                     .format(guess)).casefold()
    if high_low == "h":
        # Guess higher. The low end of the range becomes 1 greater than
        # the guess.
        low = guess + 1
        count += 1
    elif high_low == "l":
        # Guess lower.  The high end of the range becomes one less than
        # the guess.
        high = guess - 1
        count += 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(count))
        print("Goodbye!")
        break
    else:
        print("Please enter h, l, or c")
# here's a more useful and impressive use of an else in a for loop
# if the computer knows your number it can just spit it out immediately and
# this line will execute!
else:
    print("Your number is {}!".format(low))
    print("I got it in {} guesses!".format(count))
