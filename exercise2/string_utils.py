# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    return s[::-1]


    pass


def count_vowels(s: str) -> int:
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)


    pass


def is_palindrome(s: str) -> bool:
    s = s.lower()  # Convertir en minuscules
    s = ''.join(c for c in s if c.isalnum())
    return s == s[::-1]

    pass


def capitalize_words(s: str) -> str:
    return s.title()

    pass
