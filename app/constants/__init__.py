# message
ALERT_TEXT = '🚨🚨🚨🚨🚨'
VIP_TEXT = ' ⚜️ '
SAMPLE_TEXT = '''
{is_vip}بلیط اتوبوس {from_city} به {to_city}{is_vip}
🗓 زمان: {persian_date} {departure_time} تا {arrival_time}
👬 ظرفیت: {capacity}
💵 قیمت: {price} تومان
🚍 نوع اتوبوس: {bus_type}
👨🏼‍✈️ شرکت: {company}

🌐 لینک رزرو:
{reserve_link}
'''

# urls
MRBILIT_INQUIRE_URL = 'https://bus.mrbilit.ir/api/GetBusServices'
MRBILIT_RESERVE_URL = 'https://mrbilit.com/buses/{source}-{destination}?departureDate={date}'
BALE_URL = 'https://tapi.bale.ai/bot{token}/sendMessage'

# mr.bilit auth options
MRBILIT_AUTH_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJidXMiOiI0ZiIsInRybiI6IjE3Iiwic3JjIjoiMiJ9.vvpr9fgASvk7B7I4KQKCz-SaCmoErab_p3csIvULG1w"
MRBILIT_AUTH_SESSION = "session_6785c990-2e11-4aaa-9bfe-862c8abafd1c"

# others
DATE_FORMAT = '%Y-%m-%d'
REDIS_TRIP_PREFIX = 'TRIP'

try:
    from .local_constants import *
except ImportError:
    pass
