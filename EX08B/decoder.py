"""Decodes messages."""
import encoder
import filler


def _decrypt_message(encrypted_message, shift):
    """
    Decrypt encrypted message using the given shift.

    :param encrypted_message: Message which was encrypted by _encrypt_message.
    :param shift: The amount of letters needed to shift forward.
    :return: Decrypted message.
    """
    return filler.caesars_code(encrypted_message, shift)


def get_message(initial_message, shift, decrypt=False):
    """
    Get message from initial message using given shift.

    :param initial_message: The first dirty version of a message.
    :param shift: How many letters does the cipher shift
    :param decrypt: To decrypt on encrypt, that is the question
    :return: The message.
    """
    if decrypt is True:
        return _decrypt_message(encoder.get_corrected_encrypted_message(initial_message, shift), shift)
    elif decrypt is False:
        return encoder.get_corrected_encrypted_message(initial_message, shift)


print(_decrypt_message("hello world", 17))  # => qnuux fxaum
print(_decrypt_message("az!", 1))  # => zy!
print(_decrypt_message("AbCxYz", 10))  # => QrSnOp
