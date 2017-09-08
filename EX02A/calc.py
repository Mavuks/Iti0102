"""Calculate the value of z."""
import math


def value_of_z(ex, x, y):
    """
    Calculate the value of z with given x and y.

    :param ex: exercise number
    :param x: 4
    :param y: 4
    :return: float
    """
    # Your code here
    pass

    if ex is 1:
            return(x ** y + y ** x)
    elif ex is 2:
            return((x / 5.6) - (y / 6.5))
    elif ex is 3:
            return((x / 5) * y ** 4 * (math.log(5)) / (7 * math.sqrt(x ** 2 + y ** 2) + 1))
    else:
            return "sellist ülesannet ei ole!"
# testid


print(value_of_z(1, 0, 0))  # -> 2
print(value_of_z(1, 5, 10))  # -> 9865625
print(value_of_z(2, 50, 1))  # -> 8.774725274725276
print(value_of_z(3, 99, 99))  # -> 3120247.5768747954
print(value_of_z(3, 10, 10))  # -> 321.90384067126877
print(value_of_z(3, 0, 0))  # -> 0.0
print(value_of_z(4, 0, 0))  # None