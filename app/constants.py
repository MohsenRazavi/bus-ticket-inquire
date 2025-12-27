CITIES = {
    'jahrom': 41370000,
    'shiraz': 41310000
}

ALERT_TEXT = '🚨🚨🚨🚨🚨'
SAMPLE_TEXT = '''
{is_vip}بلیط اتوبوس {from_city} به {to_city}{is_vip}
🗓 زمان: {persian_date} {departure_time} تا {arrival_time}
👬 ظرفیت: {capacity}
💵 قیمت: {price} تومان
🚍 نوع اتوبوس: {bus_type}
👨🏼‍✈️ شرکت: {company}

لینک رزرو:
{reserve_link}
'''
DATE_FORMAT = '%Y-%m-%d'


MRBILIT_INQUIRE_URL = 'https://bus.mrbilit.ir/api/GetBusServices'
MRBILIT_RESERVE_URL = 'https://mrbilit.com/buses/{source}-{destination}?departureDate={date}'
BALE_URL = 'https://tapi.bale.ai/bot{token}/sendMessage'
