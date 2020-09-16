"""This will begin a new Python lesson about code blocks and flow control."""

# for i in range(1, 13):
# print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
# print("*" * 80) if this line is in the block, it will also repeat
# print("*" * 80)  # But this line will only print once

name = input("Please enter your name: ")
age = int(input(f"How old are you {name}? "))
print(age)

if age > 18:
    print("You're old enough to vote")
    print("Please put an X in the box")
elif age == 18:
    print("You just made it you 18 year old you!  Go vote!")
else:
    print("Please come back in {0} years".format(18 - age))
