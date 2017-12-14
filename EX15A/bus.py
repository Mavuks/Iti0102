"""Bussiajad."""

import datetime


class input:
    """Tere."""
    timeformat = "%H:%M"
    time = input("What's your time?")
    try:
        validtime = datetime.datetime.strptime(time, timeformat)
    except ValueError:
        print("Use HH:SS format!")


class File:
    """Loeb faili."""


class Main:
    """Main."""

    def __init__(self, file: str):
        """Tere."""