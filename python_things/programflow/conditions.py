"""And Or practice."""


age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("Have a nice day at work!")
elif age < 16:
    print("You're too young to work!")
elif age > 65:
    print("You're retired!")

print("-" * 30)

if age < 16 or age > 65:
    print("You shouldn't be working!")
else:
    print("Have a nice day at work!")
