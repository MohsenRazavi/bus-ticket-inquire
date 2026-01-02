from functools import wraps

import redis

from app.constants import REDIS_TRIP_PREFIX
from app.settings import REDIS_HOST, REDIS_PORT, REDIS_EXPIRATION_DURATION, REDIS_DB, \
    REDIS_EXCEPTION_EXPIRATION_DURATION


def with_redis(func):
    """
    FUNC MUST HAVE ARGUMENT _redis
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        _redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True, )
        return_data = func(*args, **kwargs, _redis=_redis)
        _redis.close()
        return return_data

    return wrapper


@with_redis
def trip_exists_in_redis(trip_id, _redis=None):
    redis_key = make_trip_redis_key(trip_id)
    return _redis.get(redis_key)


def make_trip_redis_key(trip_id):
    return REDIS_TRIP_PREFIX + ':' + trip_id


@with_redis
def save_trip_to_redis(trip_id, message_id, day_counter, _redis=None):
    duration = int(2 * (day_counter + 0.5) * REDIS_EXPIRATION_DURATION)
    redis_key = make_trip_redis_key(trip_id)
    _redis.set(redis_key, message_id, ex=duration)


@with_redis
def reset_redis(_redis):
    _redis.flushdb()


@with_redis
def save_exception_to_redis(exception, message_id, _redis=None):
    _redis.set(type(exception), message_id, ex=REDIS_EXCEPTION_EXPIRATION_DURATION)


@with_redis
def exception_exists_in_redis(exception, _redis=None):
    return _redis.get(type(exception))


@with_redis
def delete_trip_from_redis(trip_id, _redis=None):
    _redis.delete(make_trip_redis_key(trip_id))
