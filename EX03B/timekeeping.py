"""Timekeeping."""


def seconds(time_string, from_seconds_in_minute):
    """
    Amount seconds in time_string.

    :param time_string: current time as a time_string
    :param from_seconds_in_minute: current amount of seconds in one minute
    :return:amount seconds
    """
    a = from_seconds_in_minute
    m, s = time_string.split(':')
    return (int(m) * a + int(s))


def minute_count(time_string, from_seconds_in_minute, to_seconds_in_minute):
    """
    Amount minute in new system.

    :param time_string: current time as a time_string
    :param from_seconds_in_minute: current amount seconds in one minute
    :param to_seconds_in_minute: new amount seconds in one minute
    :return: new amount minute in new system
    """
    new = to_seconds_in_minute
    z = seconds(time_string, from_seconds_in_minute)
    k = z // new
    return k


def seconds_count(time_string, from_seconds_in_minute, to_seconds_in_minute):
    """
    Amount seconds in new system.

    :param time_string: current time as a time_string
    :param from_seconds_in_minute: current amount seconds in one minute
    :param to_seconds_in_minute: new amount seconds in one minute
    :return:new amount seconds in new system
    """
    new = to_seconds_in_minute
    z = seconds(time_string, from_seconds_in_minute)
    h = z % new
    return h


def final(time_string, from_seconds_in_minute, to_seconds_in_minute):
    """
    New time_String.

    :param time_string: current time as a time_string
    :param from_seconds_in_minute: current amount seconds in one minute
    :param to_seconds_in_minute: new amount seconds in one minute
    :return: new time_string
    """
    k = minute_count(time_string, from_seconds_in_minute, to_seconds_in_minute)
    h = seconds_count(time_string, from_seconds_in_minute, to_seconds_in_minute)
    return f'{str(k).zfill(2) }:{str(h).zfill(2)}'


def convert(time_string, from_seconds_in_minute, to_seconds_in_minute):
    """
    Convert time from one system to another.

    :param time_string: current time as a time_string
    :param from_seconds_in_minute: current amount seconds in one minute
    :param to_seconds_in_minute: new amount seconds in one minute
    :return: converted time_String
    """
    a = from_seconds_in_minute
    m, s = time_string.split(':')
    if str(s) > str(a):
        return "None"
    elif str(s) == str(a):
        return "None"

    q = minute_count(time_string, from_seconds_in_minute, to_seconds_in_minute)
    e = seconds_count(time_string, from_seconds_in_minute, to_seconds_in_minute)
    u = str(q).zfill(2)
    o = str(e).zfill(2)

    return f'{u}:{o}'


print(convert('12:12', 20, 30))
print(convert('03:40', 60, 3))
print(convert('03:61', 60, 3))
print(convert('03:40', 40, 10))
