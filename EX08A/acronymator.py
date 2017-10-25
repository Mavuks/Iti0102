
"""Turn a phrase into acronym."""


def acronymize(message: str) -> str:
    """
    Turn the input text into the acronym and reverse it, if the text is not too long.

    :param message: initial text
    :return: reversed acronym
    """



def check_word(word: str) -> bool:
    """
    Check if the word is long enough and does not contain special symbols.

    The word should be more than 3 chars long (without symbols).
    :param word: word
    :return: bool
    """
    # check_word("a-bc") -> True



def check_message_length(words: list) -> bool:
    """
    Check if the initial text length is OK (does not contain more than 50 words).

    :param words: list of words
    :return: bool
    """

    return len(words) >= 50

    # text_length = len(words.split()) > 50 == 'True'
    # print bool(text_length)
    #
    # if (bool(text_length) in True):
    #     return "Sorry, the input's just too long!"



    # text_length = len(words.split()) > 50
    # if text_length is True:
    #     return "Sorry, the input's just too long!"





def reverse(message: str) -> str:
    """
    Reverse the given message.

    :param message: acronym
    :return: reversed message
    """
    return message[::-1]




if __name__ == '__main__':


    print(reverse("Tere"))
    print(check_message_length("""
    As soon as the light in the bedroom went out there was a stirring and a
    fluttering all through the farm buildings. Word had gone round during the
    day that old Major, the prize Middle White boar, had had a strange dream
    on the previous night and wished to communicate it to the other animals.
    It had been agreed that they should all meet in the big barn as soon as
    Mr. Jones was safely out of the way."""))