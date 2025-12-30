import os

DEBUG_LOG = False
DEBUG_SEND_MESSAGE = True

ROOT = os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'), '..')
TRIPS_PATH = os.path.join(ROOT, 'trips.json')

NEXT_DAYS = 7

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

TODAY_STORING_DURATION = 2 * 60 * 60  # 2 HOURS
OTHER_DAYS_STORING_DURATION = 24 * 60 * 60  # 1 DAY

# should be filled in local_settings
BALE_TOKEN = ''
EXCEPTION_REPORT_CHAT_ID = ''

try:
    from .local_settings import *
except ImportError:
    pass