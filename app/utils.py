import json
import traceback

import requests

from app.settings import (BALE_URL, BALE_TOKEN, GROUP_CHAT_ID, INQUIRED_IDS_JSON, EXCEPTION_REPORT_CHAT_ID, MRBILIT_URL,
                          SAMPLE_TEXT, ALERT_TEXT, DEBUG)


def inquire_and_send_trips(source, destination, date):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9,fa;q=0.8",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJidXMiOiI0ZiIsInRybiI6IjE3Iiwic3JjIjoiMiJ9.vvpr9fgASvk7B7I4KQKCz-SaCmoErab_p3csIvULG1w",
        "content-type": "application/json-patch+json",
        "origin": "https://mrbilit.com",
        "referer": "https://mrbilit.com/",
        "sessionid": "session_6785c990-2e11-4aaa-9bfe-862c8abafd1c",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
        "x-playerid": "1ff829a7-e1c6-4eda-a787-26cbc48626cb",
    }

    payload = {
        "from": source,
        "to": destination,
        "date": date,
        "includeClosed": True,
        "includePromotions": True,
        "loadFromDbOnUnavailability": True,
        "includeUnderDevelopment": True
    }
    response = requests.post(MRBILIT_URL, headers=headers, json=payload)
    status = response.status_code
    if  status != 200:
        send_bale_message(f'STATUS CODE {status} !!!', exception_report=True)
    resp = response.json()
    inquired_ids: set = read_json_file()
    for bus in resp['buses']:
        id_ = bus.get('id')
        if id_ in inquired_ids:
            continue
        inquired_ids.add(id_)
        persian_date = bus.get('dateString')
        company = bus.get('corporation')
        capacity = bus.get('capacity')
        from_city = bus.get('fromCity')
        penalty_text = bus.get('penaltyText')
        price = bus.get('price')
        to_city = bus.get('toCity')
        weekday = bus.get('weekday')
        bus_type = bus.get('busType')
        is_vip = bus.get('isVIP')
        arrival_time = bus.get('arrivalTime').split('T')[1]
        departure_time = bus.get('departureTime').split('T')[1]

        alert = True if capacity < 20 else False
        sending_text = SAMPLE_TEXT.format(from_city=from_city,
                                          arrival_time=arrival_time,
                                          departure_time=departure_time,
                                          persian_date=weekday + ' ' + persian_date,
                                          capacity=capacity,
                                          price=price,
                                          bus_type=bus_type,
                                          company=company,
                                          to_city=to_city,
                                          is_vip=' ⚜️ ' if is_vip else '',
                                          )
        if penalty_text:
            sending_text = sending_text + '\n\n' + penalty_text

        if alert:
            sending_text = ALERT_TEXT + sending_text
        if DEBUG:
            print(10 * '=', )
            print(sending_text)
            print(10 * '=', end='\n\n')
        send_bale_message(sending_text)
    write_to_json_file(inquired_ids)


def send_bale_message(message, exception_report=False):
    url = BALE_URL.format(token=BALE_TOKEN)
    if exception_report:
        chat_id = EXCEPTION_REPORT_CHAT_ID
    else:
        chat_id = GROUP_CHAT_ID
    json = {'chat_id': chat_id, 'text': message}
    resp = requests.post(url, json=json)
    if DEBUG:
        print(resp.status_code)
        print(resp.text)


def read_json_file():
    try:
        with open(INQUIRED_IDS_JSON) as json_file:
            data = json.load(json_file)
            inquired_ids = set(data['ids'])
            return inquired_ids
    except Exception:
        return set()

def write_to_json_file(data):
    with open(INQUIRED_IDS_JSON, 'w') as json_file:
        json.dump({'ids': list(data)}, json_file)
