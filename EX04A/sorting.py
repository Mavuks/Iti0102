"""Sort the strings in ascending order."""


def get_min_len_word(string_list):
    """
    Function to find and return the minimum length word in string_list.

    If two Strings are the same length, the String appearing first must also
    be returned first.

    :param string_list: List of Strings to look through.
    :return: Smallest length String from string_list.
    """
    if not string_list:
        return None
    string_list.sort(key=len)
    return string_list[0]


def sort_list(string_list):
    """
    Function to sort string_list by the length of it's elements.

    This function must utilize get_min_len_word().

    :param string_list: List of Strings to be sorted.
    :return: Sorted list of Strings.
    """
    # Your Code

    sorted_list = list()
    while list:
        if not string_list:
            break

        min_word = get_min_len_word(string_list)
        sorted_list.append(min_word)
        string_list.remove(min_word)

    return sorted_list


if __name__ == '__main__':

    print(get_min_len_word(['Mary', 'had', ', 'little', 'lamb']))
    print(get_min_len_word(['Hi', 'there']))
    print(get_min_len_word(['Hello', 'there']))
    print(sort_list(['aaa', 'bb', 'c']))
    print(sort_list(['Hello', 'there']))
    print(sort_list(['Mary', 'had', 'a', 'little', 'lamb']))
    print(get_min_len_word([]))
