"""Filler for encoder and decoder."""


def get_end(piece, true_message):
    """Get end piece."""
    if piece[-1] in ("/#$%^&*@0123456789"):  # works through words with symbols at the end
        for char in range(-1, -len(piece), -1):
            if piece[char] in "/#$%^&*@0123456789":
                if char == -1:
                    true_message += piece[char]
                else:
                    true_message.insert(char + 1, piece[char])
            elif piece[char] not in ("/#$%^&*@0123456789"):
                break


def give_corrected_piece(piece):
    """Give corrected piece."""
    true_message = []
    if piece[0] in "/#$%^&*@0123456789":  # works through words with symbols at the beginning
        for char in range(len(piece)):
            if piece[char] in "/#$%^&*@0123456789":
                true_message += piece[char]
            elif piece[char] not in "/#$%^&*@0123456789":
                break
            if char == len(piece) - 1:
                true_message += " "
                return "".join(true_message)

    for char in range(len(piece)):  # works through words with no symbols at the beginning or the end
        if piece[char] not in "/#$%^&*@0123456789":
            true_message += piece[char]

    get_end(piece, true_message)
    true_message += " "

    return "".join(true_message)


def caesars_code(message, shift, encrypted=True):
    """Create Caesar's code."""
    text = ""
    if shift >= 26:
        shift %= 26

    for char in message:
        stay_in_lower, stay_in_upper = encrypt(char, encrypted, shift)
        if char.isupper():
            if stay_in_upper > 90:
                stay_in_upper -= 26
            elif stay_in_upper < 65:
                stay_in_upper += 26
            finalLetter = chr(stay_in_upper)
            text += finalLetter
        elif char.islower():
            if stay_in_lower > 122:
                stay_in_lower -= 26
            elif stay_in_lower < 97:
                stay_in_lower += 26
            finalLetter = chr(stay_in_lower)
            text += finalLetter
        else:
            text += char
    return text


def encrypt(char, encrypted, shift):
    """Check if encrypted or not."""
    if encrypted is True:
        stay_in_upper = ord(char) - shift
        stay_in_lower = ord(char) - shift
    if encrypted is False:
        stay_in_upper = ord(char) + shift
        stay_in_lower = ord(char) + shift
    return stay_in_lower, stay_in_upper
