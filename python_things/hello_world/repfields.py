"""This is a lesson on string replacements."""
age = 24
print(type(age))
print("My name is " + str(age) + " years.")
print("My name is {0} years.".format(age))

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}."
      .format(31, "Jan", "March", "May", "July", "Aug", "Oct", "Dec"))

print()
num1 = 3
num2 = 1
print(f"The sum of {num1} and {num2} is {num1 + num2}.")
print("The sum of {0} and {1} is {2}.".format(num1, num2, num1 + num2))
