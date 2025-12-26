import os

DEBUG = False

ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
INQUIRED_IDS_JSON = os.path.join(ROOT, 'inquired_ids.json')

MRBILIT_URL = 'https://bus.mrbilit.ir/api/GetBusServices'
BALE_URL = 'https://tapi.bale.ai/bot{token}/sendMessage'

CITIES = {
    'jahrom': 41370000,
    'shiraz': 41310000
}

NEXT_DAYS = 7

SAMPLE_TEXT = '''
{is_vip}بلیط اتوبوس {from_city} به {to_city}{is_vip}
🗓 زمان: {persian_date} {departure_time} تا {arrival_time}
👬 ظرفیت: {capacity}
💵 قیمت: {price} تومان
🚍 نوع اتوبوس: {bus_type}
👨🏼‍✈️ شرکت: {company}
'''

ALERT_TEXT = '🚨🚨🚨🚨🚨'

TRIPS = [
    {
        'source': CITIES['jahrom'],
        'destination': CITIES['shiraz']
    },
    {
        'source': CITIES['shiraz'],
        'destination': CITIES['jahrom']
    }
]

BALE_TOKEN = ''
GROUP_CHAT_ID = ''
EXCEPTION_REPORT_CHAT_ID = ''

try:
    from app.local_settings import *
except ImportError:
    pass