import time 
import datetime
from functools import wraps

def timer(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f"{fun.__name__} takes {end - start:.4f}s to finish")
        return result
    return wrapper

def logger(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):

        now = datetime.datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{formatted_date} [LOG] calling {fun.__name__} | args: {kwargs}")
        result = fun(*args, **kwargs)
        return result
    return wrapper
