"""Casidoo challenge for number of characters."""
# Given a string s and a character c, return the number of occurrences
# of c in s.
# Ex: num_chars('oh heavens', 'h')
# => 2


def num_chars(phrase, letter):
    """Count the number of a given letter in a phrase."""
    counter = 0
    for char in phrase:
        if char.casefold() == letter.casefold():
            counter += 1
    return counter


print(num_chars('oh heavens', 'h') == 2)
print(num_chars('she sells seashells down by the seashore', 's') == 8)
