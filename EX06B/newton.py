"""Calculate square root with Newton method."""


def square_root_with_newton_method(number, iterations):
    """
    Calculate the given number's approximate square root.

    :param number: number from which the square root will be calculated.
    :param iterations: number of formula cycles, highest integer not bigger than the value (1.9 => 1).
    :return: approximate square root. In the case of non-positive number or negative iterations, return None.
    """
    # Inital value of g.
    # Cycle based on the iterations number.
    # Formula in the cycle.
    # Return the rounded final result.

    if number <= 0 or iterations < 0:
        return None
    g = number * 0.5
    for i in range(int(iterations)):
        g2 = (g + number / g) * 0.5
        g = g2
    return round(g, 3)

if __name__ == '__main__':
    print(square_root_with_newton_method(0.9, 1))