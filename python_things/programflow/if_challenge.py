"""Challenge using if."""
# Write a small program to ask for a name and an age
# When both values have been entered check if the person is the
# right age to go on an 18-30 holiday (whatever that is).
# If a person is over 18 and under 31 invite them.
# If they are under 18 or over 31 refuse them entry.

name = input("Hello, what is your name? ")
print(f"And how old are you {name}?")
age = int(input())

if age >= 18 and age < 31:
    print("{} you qualify for an 18-30 holiday!  Pack your bags!".format(name))
else:
    print("Sorry, you don't qualify for an 18-30 holiday.")
