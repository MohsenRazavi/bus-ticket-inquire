import os

DEBUG_LOG = False
DEBUG_SEND_MESSAGE = True
DEBUG_SAVE_TO_REDIS = True


ROOT = os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'), '..')
TRIPS_PATH = os.path.join(ROOT, 'trips.json')

NEXT_DAYS = 7

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

REDIS_EXPIRATION_DURATION = 1 * 60 * 60  # 1 HOURS
REDIS_EXCEPTION_EXPIRATION_DURATION = 1 * 60 * 60
# should be filled in local_settings
BALE_TOKEN = ''
EXCEPTION_REPORT_CHAT_ID = ''

try:
    from .local_settings import *
except ImportError:
    pass