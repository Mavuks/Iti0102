
"""Recursion vs loops."""


def loop_reverse(s: str) -> str:
    """
    Reverse a string using a loop.

    :param s: input string
    :return: reversed input string
    """
    a = ""
    for i in range(1, len(s) + 1):
        a += s[len(s) - i]
    return a


def recursive_reverse(s: str) -> str:
    """
    Reverse a string using recursion.

    :param s: input string
    :return: reversed input string
    """
    pass


def loop_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using a loop.

    :param n: the last number to add to the sum
    :return: sum
    """
    pass


def recursive_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using recursion.

    :param n: the last number to add to the sum
    :return: sum
    """
    pass


if __name__ == '__main__':
    print(loop_reverse("hello"))  # -> "olleh"
    print(recursive_reverse("A"))  # -> "A"
    print(recursive_reverse(""))  # -> ""
    print(loop_sum(3))  # -> 6
    print(recursive_sum(95))  # -> 4560
    print(recursive_sum(0))  # -> 0
