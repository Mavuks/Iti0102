"""Retrieve stops and departures info from REST service."""
import json
import urllib.request

API_BASE = "https://public-transport-api.herokuapp.com"
REGION = "tallinn"


def get_nearby_stops(api_base, lat, lng):
    """
    Get nearby stops.

    :param api_base: Base URL that the endpoint gets appended to
    :param lat: Latitude
    :param lng: Longitude
    :return: List of all nearby stops
    """
    if api_base == "" or lat == "" or lng == "":
        return None
    with urllib.request.urlopen(api_base + "/stops/" + str(lat) + "/" + str(lng)) as f:
        contents = f.read()
        data = json.loads(contents.decode('utf-8'))
        sorted_data = sorted(data, key=lambda x: int(x['distance'].split(" ")[0]))

    return sorted_data


def get_nearest_stop(api_base, lat, lng):
    """
    Get nearest stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param lat: Latitude
    :param lng: Longitude
    :return: Nearest stop
    """
    try:
        return get_nearby_stops(api_base, lat, lng)[0]
    except Exception:
        return None


def get_next_departures(api_base, region, stop_id):
    """
    Get next departures from stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param region: Region
    :param stop_id: Stop ID
    :return: List of next departures from stop
    """
    if api_base == "" or stop_id == "" or region == "":
        return None
    with urllib.request.urlopen(api_base + "/departures/" + region + "/" + str(stop_id)) as f:
        contents = f.read()
        data = json.loads(contents.decode('utf-8'))
    return data['departures']


def get_next_departure(api_base, region, stop_id):
    """
    Get next departure from stop.

    :param api_base: Base URL that the endpoint gets appended to
    :param region: Region
    :param stop_id: Stop ID
    :return: Next departure from stop
    """
    try:
        return get_next_departures(api_base, region, stop_id)[0]
    except Exception:
        return None


if __name__ == '__main__':
    print(get_nearby_stops(API_BASE, 59.3977111, 24.660198))
    print(get_nearest_stop(API_BASE, 59.3977111, 24.660198))
    print(get_next_departures(API_BASE, REGION, get_nearest_stop(API_BASE, 59.3977111, 24.660198)["id"]))
    print(get_next_departure(API_BASE, REGION, get_nearest_stop(API_BASE, 59.3977111, 24.660198)["id"]))
