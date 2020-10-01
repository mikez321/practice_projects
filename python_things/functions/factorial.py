"""Factorial function fun."""


def factorial(num: int) -> int:
    """
    Find the factorial of a given number.

    :param num: This number is the number to find the factorial from.
    :return: The return is an integer that is the factorial of the given num.
    """
    result = 1
    if 0 <= num <= 1:
        return result
    else:
        numbers = list(range(1, num + 1))
        for i in numbers:
            result *= i
        return result


print(factorial(4))
