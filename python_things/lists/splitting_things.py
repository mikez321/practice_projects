"""Split things up using split()."""
panagram = """The quick brown
              fox jumps over\tthe lazy
              brown dog."""

words = panagram.split()
print(words)

number = '9,344,820,194,001,873'
digit_list = number.split(',')
print(digit_list)
rejoined_numbers = "".join(digit_list)
print(rejoined_numbers)
print('*' * 5 + ' Challenge Below! ' + '*' * 5)
# splitting a string returns a list of strings. Use a for loop
# and split that number into a list of ints.
int_list = []
for group in digit_list:
    int_list.append(int(group))

print(int_list)
