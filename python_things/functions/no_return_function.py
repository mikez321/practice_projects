"""Not all functions return something even if they do something."""
phrase = "I'm totally making up this lesson."
print(phrase)
split_phrase = phrase.split()
print(split_phrase)
# The return value of the sort method is None
# but it sorts the list and mutates it
print(split_phrase.sort())

# Even if you assign a variable, the variable will be
# assigned the output which is none.
sorted_phrase = split_phrase.sort()
print(sorted_phrase)

# But then if you just print the mutates split phrase
# it prints as expected
split_phrase.sort()
print(split_phrase)
