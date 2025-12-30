import requests

from app.constants import BALE_URL
from app.settings import BALE_TOKEN, EXCEPTION_REPORT_CHAT_ID, DEBUG_SEND_MESSAGE, DEBUG_LOG


def send_bale_message(chat_id: int, message: str):
    url = BALE_URL.format(token=BALE_TOKEN)
    json = {'chat_id': chat_id, 'text': message}
    if DEBUG_SEND_MESSAGE:
        resp = requests.post(url, json=json)
        if DEBUG_LOG:
            print(resp.status_code)
            print(resp.text)
        return resp.json()


def send_exception_message(message: str):
    url = BALE_URL.format(token=BALE_TOKEN)
    json = {'chat_id': EXCEPTION_REPORT_CHAT_ID, 'text': message}
    if DEBUG_LOG:
        print(f'!!! REPORT EXCEPTION !!!\n\n{message}')
    if DEBUG_SEND_MESSAGE:
        resp = requests.post(url, json=json)
        if DEBUG_LOG:
            print(resp.status_code)
            print(resp.text)
        return resp