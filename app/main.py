import traceback
from datetime import datetime, timedelta

from app.settings import NEXT_DAYS
from app.utills.bale import send_exception_message
from app.utills.inquiry import inquire_and_notify_trips
from app.utills.trip import read_trips


def main():
    date_ = datetime.today()
    for i in range(NEXT_DAYS):
        date_ = date_ + timedelta(days=1)
        date_stamp = datetime.timestamp(date_)
        trips = read_trips()
        for trip in trips:
            try:
                inquire_and_notify_trips(trip, date_stamp=date_stamp, day_counter=i)
            except Exception:
                send_exception_message(traceback.format_exc(limit=4000))


if __name__ == '__main__':
    main()
