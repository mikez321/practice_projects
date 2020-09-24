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
