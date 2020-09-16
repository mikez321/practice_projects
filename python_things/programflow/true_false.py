"""Practice with Booleans."""


# day = "Monday"
# temperature = 30
# raining = True
#
# if day == "Saturday" and temperature > 27 and not raining:
#     print("Go Swimming")
# else:
#     print("Learn Python")
name = print("Please enter your name: ")
# I did this with name = int(input()) and if you enter
# a 0 as the name, it does evaluate to false.  Neat!
if name:
    print("Hello {}".format(name))
else:
    print("Totes False")
