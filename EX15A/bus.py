"""When will my bus leave?."""


class Main:
    """Main class."""

    def __init__(self, file: str):
        """initi."""

        self.given_minutes = 0
        self.closest_time = 0
        self.departing_minutes = self.format_text(file)

    def format_text(self, file: str):
        """Format text."""

        departing_minutes = []
        with open(file) as text:
            for line in text:
                split_data = line.split()
                for minute in split_data[1:]:
                    departing_minutes.append(int(split_data[0]) * 60 + int(minute))
        return departing_minutes

    def get_closest_time(self):
        """Get closest time."""
        departing = ""
        for leaving in self.departing_minutes:
            if leaving > self.given_minutes % max(self.departing_minutes):
                departing = leaving
                break
        return departing

    def get_departure_time(self):
        """Get depature time."""
        given_time = self.ask_user_time()
        self.given_minutes = given_time[0] * 60 + given_time[1]
        self.closest_time = self.get_closest_time()
        hours = self.closest_time // 60
        minutes = str(self.closest_time % 60).zfill(2)
        print("Your bus will depart at {HH}:{mm}".format(HH=hours, mm=minutes))
        return "Your bus will depart at {HH}:{mm}".format(HH=hours, mm=minutes)

    def ask_user_time(self):
        """User time."""

        given_time = input()
        if ":" in given_time:
            given_time = given_time.split(":")
            if given_time[0].isnumeric() and given_time[1].isnumeric():
                if 1 <= len(given_time[0]) <= 2 and len(given_time[1]) == 2:
                    if 0 <= int(given_time[0]) < 25 and 0 <= int(given_time[1]) <= 59:
                        return int(given_time[0]), int(given_time[1])
        raise Exception



Main("bussiajad.txt").get_departure_time()