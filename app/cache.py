import time

cache = {}
TTL = 10  # seconds


def get_cached(key, fetch_func):
    now = time.time()

    if key in cache and now - cache[key]["time"] < TTL:
        return cache[key]["data"]

    data = fetch_func()

    cache[key] = {
        "data": data,
        "time": now
    }

    return data