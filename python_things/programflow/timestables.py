"""Use nested for statements to make times tables."""
for i in range(1, 13):
    print("*" * 5 + " {} times tables ".format(i) + "*" * 5)
    for j in range(1, 13):
        print("{0} times {1} is {2}".format(j, i, j * i))
    print("\n" * 2)
