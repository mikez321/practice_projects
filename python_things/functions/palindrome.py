"""Explore functions and palindromes."""


def is_palindrome(word):
    """Determine if a word is the same forwards and backwards."""
    return word.casefold() == word[::-1].casefold()


word = input("Please enter a word to check: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
