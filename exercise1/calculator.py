# Exercise 1: Basic Calculator Functions
from typing import Union

# Defining a Number type for cleaner type hints
Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    "cette fonction prends comme arguments deux nombres et retourne leur somme qui est un nbre aussi""
    Return the sum of a and b.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    
    return a+b
    
    


def subtract(a: Number, b: Number) -> Number:
    """
    Return the result of subtracting b from a.

    Args:
        a: First number
        b: Second number

    Returns:
        The result of a - b
    """
    
    return a-b
    pass


def multiply(a: Number, b: Number) -> Number:
    """
    Return the product of a and b.

    Args:
        a: First number
        b: Second number

    Returns:
        The product of a and b
    """
  
    return a*b
    pass


def divide(a: Number, b: Number) -> Number:
    """
    Return the result of dividing a by b.

    Args:
        a: First number (dividend)
        b: Second number (divisor)

    Returns:
        The result of a / b

    Raises:
        ValueError: If b is 0
    """
    if b=0:
        raise ValueError("Division by zero is not allowed")  # Correction du retour d'erreur 
    return a/b
    
    pass
