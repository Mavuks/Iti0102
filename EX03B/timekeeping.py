def convert(time_string, from_seconds_in_minute, to_seconds_in_minute):
    a = from_seconds_in_minute
    m, s = time_string.split(':')
    if int(s) > int(a):
        return "None"
    else:
        return(int(m) * a + int(s))


def minute_count(time_string, from_seconds_in_minute, to_seconds_in_minute):
    new = to_seconds_in_minute
    z = convert(time_string, from_seconds_in_minute, to_seconds_in_minute)
    k = z // new
    return k

def seconds_count(time_string, from_seconds_in_minute, to_seconds_in_minute):
    new = to_seconds_in_minute
    z = convert(time_string, from_seconds_in_minute, to_seconds_in_minute)
    h = z % new
    return h

def final(time_string, from_seconds_in_minute, to_seconds_in_minute):
    k = minute_count(time_string, from_seconds_in_minute, to_seconds_in_minute)
    h = seconds_count(time_string, from_seconds_in_minute, to_seconds_in_minute)
    return f'{str(k).zfill(2) }:{str(h).zfill(2) }'

'''
print(final('12:12', 20, 30))
print(final('03:40', 60, 3))
print(convert('03:61', 60, 3))
'''