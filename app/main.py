import traceback
from datetime import datetime, timedelta

from app.settings import TRIPS, NEXT_DAYS
from app.utils import send_bale_message, inquire_and_send_trips, read_json_file


def main():
    date_ = datetime.today()
    for i in range(NEXT_DAYS):
        date_ = date_ + timedelta(days=1)
        for trip in TRIPS:
            try:
                inquire_and_send_trips(date=date_.strftime('%Y-%m-%d'), **trip)
                raise
            except Exception:
                send_bale_message(traceback.format_exc(limit=4000), exception_report=True)


if __name__ == '__main__':
    main()
