# temperature.py
print ('temperature module loaded and ready!')
def convert_to_celsius(fahrenheit):
    """ (number) -> float
    Return the number of Celsius degrees equivalent to fahrenheit
    degrees.
    >>> convert_to_celsius(75)
    23.88888888888889
    """
    return (fahrenheit - 32.0) * 5.0 / 9.0
def above_freezing(celsius):
    """ (number) -> bool
    Return True iff temperature celsius is above freezing.
    >>> above_freezing(5.2)
    True
    >>> above_freezing(-2)
    False
    """
    return celsius > 0

# run only first time
if __name__ == '__main__':
    fahrenheit= float(input('Enter the temperature in degrees Fahrenheit: '))
    celsius = convert_to_celsius(fahrenheit)
    if above_freezing(celsius):
        print('It is ABOVE freezing.')
    else:
        print('It is below freezing.')
