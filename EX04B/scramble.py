import random

def scramble_sentence(sentence: str) -> str:
    """
    Function to change all words in sentence using scramble_word() function.

    :param sentence: sentence to scramble
    :return: scrambled sentence
    """
    # Your code
    pass


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
    foo1 = list(word[1:-2])
    foo = list(word[1:-1])
    foo.sort()
    foo1.sort()
    if word[-1] == "." or "," or "!" or "?" or ";" or "," or '"':
        return word[0] + ''.join(foo1) + word[-2]
    else:
        return word[0] + ''.join(foo) + word[-1]




if __name__ == '__main__':
   # print(scramble_sentence("Hey, how's it going?"))  # -> Hey, how's it ginog?
    #print(scramble_sentence("The phenomenal power of the human mind."))  # -> The phenomenal peowr of the hamun mind.
    print(scramble_word("putukas"))
    print(scramble_word("lammas."))
    print(scramble_word("lammas!"))
    #print(scramble_word("Mo'uSE!"))  # -> Mo'SuE!
    #print(scramble_word("CoOol"))  # -> "CoOol"
