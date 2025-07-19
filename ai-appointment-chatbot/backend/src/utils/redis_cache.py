from redis import Redis
from functools import wraps
import json

class RedisCache:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis = Redis(host=host, port=port, db=db)

    def set(self, key, value, expiration=None):
        if isinstance(value, dict):
            value = json.dumps(value)
        self.redis.set(key, value, ex=expiration)

    def get(self, key):
        value = self.redis.get(key)
        if value is not None:
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return value
        return None

    def delete(self, key):
        self.redis.delete(key)

    def clear(self):
        self.redis.flushdb()

def cache_result(expiration=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{func.__name__}:{args}:{kwargs}"
            cached_result = redis_cache.get(key)
            if cached_result is not None:
                return cached_result
            result = func(*args, **kwargs)
            redis_cache.set(key, result, expiration)
            return result
        return wrapper
    return decorator

redis_cache = RedisCache()