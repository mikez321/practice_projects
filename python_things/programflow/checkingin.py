"""Explore the in and not in statements."""

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

# if letter in parrot:
#     print(f"{letter} is in {parrot}")
# else:
#     print("I don't need that letter.")

if letter.casefold() not in parrot.casefold():
    # casefold() is a method that converts strings to lower case
    print(f"{letter} is not in {parrot}")
else:
    print("I need that letter.")
