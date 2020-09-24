"""Enumerate lesson."""
# for index, character in enumerate('abcdefgh'):
# print(index, character)
for t in enumerate('abcdefgh'):
    index, character = t
    print(index, character)
# the code above is illustrating that the enumerate function
# creates a tuple of the index and character and they can then
# be accessed by unpacking said tuple into variables.
