"""scrable."""


def scramble_sentence(sentence: str) -> str:
    """
    Function to change all words in sentence using scramble_word() function.

    :param sentence: sentence to scramble
    :return: scrambled sentence
    """
    # Your code
    pass
    lause_list = sentence.split()
    return_list = []
    for lause in lause_list:
        return_list.append(scramble_word(lause))
    return ' '.join(return_list) + sentence[-1]


def scramble_word(word: str) -> str:
    """
    Sort a word alphabetically, keeping only the astrophe, first and last letter as they were.

    If the last letter of a word is a symbol (.,;?!") the second to last letter must remain the same.
    If the length of the word without symbols is greater than 7 or the word can't be changed from the
    original, the initial word must be returned. When sorting, treat every letter as lowercase.

    :param word: input word
    :return: alphabetically scrambled word
    """
    # Your code
    i = 0
    for c in word:
        if not c.isalpha():
            i += 1
    if len(word) - i > 7 or len(word) - i <= 3:
        return word

    if word[-1].isalpha():
        foo = list(word[1:-1])
        foo = sorted(foo, key=str.lower)
        bacon = -1
    else:
        foo = list(word[1:-2])
        foo = sorted(foo, key=str.lower)
        bacon = -2

    if word.find("'") == -1:
        return word[0] + ''.join(foo) + word[bacon:]
    else:
        k = word.index("'")
        n = word.replace("'", "")
        sorted_word = word[0] + ''.join(sorted(n[1:bacon], key=str.lower)) + word[bacon:]
        sorted_list = list(sorted_word)
        sorted_list.insert(k, "'")
        return ''.join(sorted_list)


if __name__ == '__main__':
    print(scramble_sentence("Hey, how's it going?"))  # -> Hey, how's it ginog?
    print(scramble_sentence("The phenomenal power of the human mind."))  # -> The phenomenal peowr of the hamun mind.
    print(scramble_word("putukas"))
    print(scramble_word("lammas."))
    print(scramble_word("lammas!"))
    print(scramble_word("Lammas;"))
    print(scramble_word("Mo'uSE!"))  # -> Mo'SuE!
    print(scramble_word("CoOol"))  # -> "CoOol"
    print(scramble_word("don't,"))
    print(scramble_word("phenomena"))
    #Test
