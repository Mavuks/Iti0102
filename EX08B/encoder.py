"""Encodes message."""
import filler


def _correct_message(message):
    """
    Turn given message into a readable one.

    :param message: Given message.
    :return: The corrected message.
    """
    true_message = []
    words = message.split(" ")
    for word in words:
        true_message.append(filler.give_corrected_piece(word))
    return "".join(true_message)[:-1]


def _encrypt_message(message, shift):
    """
    Encrypt message using Caesar's cipher.

    :param message: Given message to encrypt.
    :param shift: How many letters to shift.
    :return: Encrypted message.
    """
    return filler.caesars_code(message, shift, False)


def get_corrected_encrypted_message(initial_message, shift):
    """
    Correct message and then encrypt it.

    :param initial_message: The dirty part of the message.
    :param shift: The amount of letters shifted in cipher.
    :return: Corrected encrypted message.
    """
    return _encrypt_message(_correct_message(initial_message), shift)


print(_encrypt_message("hello world!", 19)) # => axeeh phkew!
print(_encrypt_message("az!", 1)) # => ba!
print(_encrypt_message("AbCxYz", 10)) # => KlMhIj