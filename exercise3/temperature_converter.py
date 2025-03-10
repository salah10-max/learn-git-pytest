# Exercise 3: Temperature Converter
from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    return round(celsius * 9 / 5 + 32, 2)



def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    return round((fahrenheit-32)*5/9)

    pass


def celsius_to_kelvin(celsius: Temperature) -> float:
    return celsius+273.5

    pass


def kelvin_to_celsius(kelvin: Temperature) -> float:
    return kelvin - 273.5
    pass
