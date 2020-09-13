"""This is a continuation of the Udemy strings lessons for Python."""
parrot = 'Norwegian Blue'
# print(parrot)
# print(parrot[3])
# The above code works just like in Ruby and indexing starts at 0
# print(parrot.slice(0, 6))
# print(parrot[0])
# print(parrot[1])
# print(parrot[1])
# print(parrot[10])

# print(parrot.slice(10, 14))
# print(parrot[10:14])
#
# print(parrot[:6:2])
#
# number = "9,223,372,036,854,775,807"
#
# print(number[1::4])
# this prints only the commas... kinda cool


letters = 'abcdefghijklmnopqrstuvwxyz'
# backwards = letters[25::-1]
# print(backwards)

qpo = letters[16:13:-1]
print(qpo)
edcba = letters[4::-1]
print(edcba)
last8 = (letters[::-1])[:8]
print(last8)
