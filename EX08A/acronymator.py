"""Turn a phrase into acronym."""

import re


def acronymize(message: str) -> str:
    """
    Turn the input text into the acronym and reverse it, if the text is not too long.

    :param message: initial text
    :return: reversed acronym
    """
    word_list = message.split()

    if check_word(message) is None:
        return ''
    if check_message_length(word_list) is False:
        return "Sorry, the input's just too long!"
    checked_words = [word for word in word_list if check_word(word)]
    acronym = "".join([word[0].upper() for word in checked_words])
    return reverse(acronym)


def check_word(word: str) -> bool:
    """
    Check if the word is long enough and does not contain special symbols.

    The word should be more than 3 chars long (without symbols).
    :param word: word
    :return: bool
    """
    checked_word = re.match("([^()1234567890!?_@#$%^&*.,']+)[()1234567890!?_@#$%^&*.,']*",  word)

    if checked_word is None:
        return False
    return checked_word.group(0) == word and len(checked_word.group(1)) > 3


def check_message_length(words: list) -> bool:
    """
    Check if the initial text length is OK (does not contain more than 50 words).

    :param words: list of words
    :return: bool
    """
    if len(words) > 50:
        return False
    else:
        return True


def reverse(message: str) -> str:
    """
    Reverse the given message.

    :param message: acronym
    :return: reversed message
    """
    return message[::-1]
