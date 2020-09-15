"""This will begin a new Python lesson about code blocks and flow control."""

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))
    # print("*" * 80) if this line is in the block, it will also repeat
print("*" * 80)  # But this line will only print once
