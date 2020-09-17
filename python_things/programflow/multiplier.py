"""I thought this was cool."""
# Straight from one of the Udemy lessons:
# Early computers could only performa addition.  In order to multiply one
# number by another, they performaed repeated addition.
# For example 5 * 8 was performed by adding 5 8 times:
# 5 + 5 + 5 + 5 + 5 + 5 + 5 + 5 = 40

# Use a loop and agument assignment to find the propduct of 5 and 8

number = 5
multiplier = 8
answer = 0
# while loop:
# while multiplier != 0:
#     multiplier -= 1
#     answer += number
#
# print(answer)

# for loop
# for i in range(multiplier):
#     answer += number

# print(answer)

# recursive funtction below:


def continued_addition(times, number, answer=0):
    """Recursively adds a number n times."""
    if times == 0:
        print(answer)
    else:
        answer += number
        times -= 1
        continued_addition(times, number, answer)


continued_addition(8, 5)
