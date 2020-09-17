"""This is a Udemy lesson about the escape character."""
split_string = "This string has been \nsplit over \nseveral \nlines"
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

print('The pet shop owner said "No, no, \'e\'s uh,... he\'s resting".')
# or
print("The pet shop owner said \"No, no 'e 's uh,... he's resting\".")
print("""The pet shop owner said "No, no, 'e's uh,... he's resting".""")
# this is some kinda fancy triple quote stuff!
another_split_string = """This string has been \
split over \
several
lines"""
print(another_split_string)
# and this is how you can print a \ in your code
# print("C:\Users\timbuchalka\notes.txt")
print("C:\\Users\\timbuchalka\\notes.txt")
print(r"C:\Users\timbuchalka\notes.txt")
