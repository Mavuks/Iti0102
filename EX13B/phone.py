"""Phone."""

from functools import lru_cache


@lru_cache(maxsize=1000)
def how_many_calls(n):
    """
    Return the number of calls made during the current minute.

    Arguments:
    n -- the current minute.
    """
    if type(n) != int:
        return None
    elif n < 0:
        return None
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n > 3:
        return int (how_many_calls(n - 1) + how_many_calls(n - 2) + how_many_calls(n - 3))

@lru_cache(maxsize = 1000)
def how_many_people(n):
    """
    Return the number of people who know after n minutes has passed.

    Arguments:
    n -- how many minutes has passed.
    """
    if type(n) != int:
        return None
    elif n < 0:
        return None
    elif n == 0:
        return 1
    elif n == 1:
        return 2
    elif n > 1:
         return how_many_people(n - 1) + how_many_calls(n)






if __name__ == "__main__":
    print(how_many_calls(2))  # -> 2
    print(how_many_calls(4))  # -> 7
    print(how_many_calls(10))  # -> 274
    print(how_many_people(1))  # -> 4
    print(how_many_people(4))  # -> 15
    print(how_many_people(10))  # -> 600