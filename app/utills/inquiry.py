import datetime

import jdatetime
import requests

from app.constants import MRBILIT_INQUIRE_URL, SAMPLE_TEXT, ALERT_TEXT, MRBILIT_RESERVE_URL, DATE_FORMAT, \
    VIP_TEXT, MRBILIT_AUTH_TOKEN, MRBILIT_AUTH_SESSION
from app.settings import (DEBUG_LOG)
from app.utills.bale import send_bale_message, send_exception_message
from app.utills.redis import save_trip_to_redis, trip_exists_in_redis
from app.utills.trip import Trip


def inquire_and_notify_trips(trip: Trip, date_stamp: float, today: bool):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,fa;q=0.8",
        "authorization": MRBILIT_AUTH_TOKEN,
        "content-type": "application/json-patch+json",
        "origin": "https://mrbilit.com",
        "referer": "https://mrbilit.com/",
        "sessionid": MRBILIT_AUTH_SESSION,
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
        "x-playerid": "1ff829a7-e1c6-4eda-a787-26cbc48626cb",
    }

    payload = {
        "from": trip.source.code,
        "to": trip.destination.code,
        "date": datetime.datetime.fromtimestamp(date_stamp).strftime(DATE_FORMAT),
        "includeClosed": True,
        "includePromotions": True,
        "loadFromDbOnUnavailability": True,
        "includeUnderDevelopment": True
    }
    response = requests.post(MRBILIT_INQUIRE_URL, headers=headers, json=payload)
    status = response.status_code
    if  status != 200:
        debug_payload = {
            "from": trip.source.code,
            "to": trip.destination.code,
            "date": datetime.datetime.fromtimestamp(date_stamp).strftime(DATE_FORMAT),
        }
        report_message = f'MR.BILIT STATUS CODE {status} !!!\n\n{response.text}\npayload:\n{debug_payload}'
        if DEBUG_LOG:
            print(report_message)
        send_exception_message(report_message)
    resp = response.json()
    for bus in resp['buses']:
        id_ = str(bus.get('id'))
        if trip_exists_in_redis(id_):
            continue
        capacity = bus.get('capacity')
        alert = True if capacity and capacity < 20 else False
        link = MRBILIT_RESERVE_URL.format(source=trip.source.name, destination=trip.destination.name,
                                          date=jdatetime.datetime.fromtimestamp(date_stamp).strftime(DATE_FORMAT))
        sending_text = SAMPLE_TEXT.format(from_city=bus.get('fromCity'),
                                          arrival_time= bus.get('arrivalTime').split('T')[1],
                                          departure_time=bus.get('departureTime').split('T')[1],
                                          persian_date=bus.get('weekday') + ' ' + bus.get('dateString'),
                                          capacity=capacity,
                                          price=bus.get('price'),
                                          bus_type=bus.get('busType'),
                                          company=bus.get('corporation'),
                                          to_city=bus.get('toCity'),
                                          is_vip=VIP_TEXT if bus.get('isVIP') else '',
                                          reserve_link=link
                                          )
        if alert:
            sending_text = ALERT_TEXT + sending_text
        if DEBUG_LOG:
            print(10 * '=', )
            print(sending_text)
            print(10 * '=', end='\n\n')
        message_id = send_bale_message(trip.report_chat_id, sending_text)['result']['message_id']
        save_trip_to_redis(id_, message_id, today=today)
