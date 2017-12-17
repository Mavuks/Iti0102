"""Bussiajad."""

import datetime


class Input:
    """Tere."""

    timeformat = "%H:%M"
    time = input("What's your time?")
    try:
        validtime = datetime.datetime.strptime(time, timeformat)
    except ValueError:
        print("Use HH:SS format!")


# class File:
#     """Loeb faili."""
#     with open("bussiajad.txt") as f:


class Main:
    """Main."""

    def __init__(self, file: str):
        """Tere."""
        self.info_dict = {}
        with open(file, 'r') as f:
            self.file_lines = f.readlines()


    def dict(self):
        """Dict."""
        for line in self.file_lines:
            new_list = line.split('\t')
            self.info_dict[new_list[0]] = new_list[1:]
        return self.info_dict

    def get_departure_time(self):
        """Tere."""

