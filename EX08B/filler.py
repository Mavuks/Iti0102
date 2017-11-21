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


