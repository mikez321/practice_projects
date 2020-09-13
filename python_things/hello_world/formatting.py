"""A lesson about formatting strings."""
#  {1:3} is an example of how to change spacing of digits
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}"
          .format(i, i ** 2, i ** 3))

print()

#  <, >, and ^ will justify text so it lines up and is easier to read
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}"
          .format(i, i ** 2, i ** 3))

print()

print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12.9f}".format(22 / 7))
# print("Pi is approximately {0:12.50f}".format(22 / 7))
# print("Pi is approximately {0:52.50f}".format(22 / 7))
# print("Pi is approximately {0:22.50f}".format(22 / 7))
# print("Pi is approximately {0:54.50f}".format(22 / 7))
