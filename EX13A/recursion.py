
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
    if s == "":
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]


def loop_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using a loop.

    :param n: the last number to add to the sum
    :return: sum
    """
    sum = 0
    while(n > 0):
        sum += n
        n -= 1
    return sum


def recursive_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using recursion.

    :param n: the last number to add to the sum
    :return: sum
    """
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)


if __name__ == '__main__':
    print(loop_reverse("hello"))  # -> "olleh"
    print(recursive_reverse("A"))  # -> "A"
    print(recursive_reverse(""))  # -> ""
    print(recursive_reverse("Tere, olen Märten.."))
    print(loop_sum(3))  # -> 6
    print(recursive_sum(95))  # -> 4560
    print(recursive_sum(0))  # -> 0
