"""Sort the strings in ascending order."""


def get_min_len_word(string_list):

    """
    Function to find and return the minimum length word in string_list.

    If two Strings are the same length, the String appearing first must also
    be returned first.

    :param string_list: List of Strings to look through.
    :return: Smallest length String from string_list.
    """

    print(min((word for word in string_list if word), key=len))


def sort_list(string_list):
    """
    Function to sort string_list by the length of it's elements.

    This function must utilize get_min_len_word().

    :param string_list: List of Strings to be sorted.
    :return: Sorted list of Strings.
    """
    # Your Code
    string_list.sort(key=len)
    print(string_list)

if __name__ == '__main__':


    get_min_len_word(['Mary', 'had', 'a', 'little', 'lamb'])
    get_min_len_word(['Hi', 'there'])
    get_min_len_word(['Hello', 'there'])
    sort_list(['aaa', 'bb', 'c'])
    sort_list(['Hello', 'there'])
    sort_list(['Mary', 'had', 'a', 'little', 'lamb'])