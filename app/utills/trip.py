import dataclasses
import json

from app.settings import TRIPS_PATH


@dataclasses.dataclass
class City:
    name: str
    code: str


class Trip:
    def __init__(self, source_city, destination_city, report_chat_id):
        self.source = source_city
        self.destination = destination_city
        self.report_chat_id = report_chat_id


def read_trips():
    with open(TRIPS_PATH, "r") as f:
        trips_dict = json.load(f)
    trips = []
    for trip in trips_dict:
        source_city = City(trip['source_city']['name'], trip['source_city']['code'])
        destination_city = City(trip['destination_city']['name'], trip['destination_city']['code'])
        trips.append(Trip(source_city, destination_city, trip['report_chat_id']))
    return trips
