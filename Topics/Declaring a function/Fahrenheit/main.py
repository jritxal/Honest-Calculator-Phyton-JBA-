constant = 32
multiplier = 5 / 9


def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - constant) * multiplier, 3)
