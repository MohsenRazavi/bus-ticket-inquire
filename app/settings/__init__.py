import os

DEBUG = False
SEND_MESSAGE = True

ROOT = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..')
INQUIRED_IDS_JSON = os.path.join(ROOT, 'inquired_ids.json')
TODAY_INQUIRED_IDS_JSON = os.path.join(ROOT, 'today_inquired_ids.json')

NEXT_DAYS = 7

# will be filled in local_settings
BALE_TOKEN = ''
GROUP_CHAT_ID = ''
EXCEPTION_REPORT_CHAT_ID = ''
TRIPS = []


try:
    from .local_settings import *
except ImportError:
    pass