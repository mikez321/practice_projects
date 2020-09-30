"""Explore functions and palindromes."""


def is_palindrome(word: str) -> bool:
    """Determine if a word is the same forwards and backwards."""
    return word.casefold() == word[::-1].casefold()


def palindrome_sentence(sentence):
    """Determine if a sentence is a palendrome or not."""
    only_letters = ""
    for char in sentence:
        if char.isalpha() or char.isnumeric():
            only_letters += char
    return is_palindrome(only_letters)


# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print(f"'{word}' is a palindrome.")
# else:
#     print(f"'{word}' is not a palindrome.")

sentence = input("Enter a whole sentence to check: ")

if palindrome_sentence(sentence):
    print(f"'{sentence}' is a palindrome.")
else:
    print(f"'{sentence}' is not a palindrome.")
