
import time 
import datetime
from functools import wraps
import asyncio



def retry(n):
    def decorator(fun):
        @wraps(fun)
        async def wrapper(*args, **kwargs):
            for i in range(n):
                try:
                    
                    result = await fun(*args, **kwargs)
                    return result 
    
                except Exception as e:
                    if i == n-1:
                        raise 
                    else:
                        print("retrying....")
                        continue
        return wrapper
    return decorator




def timer(fun):
    @wraps(fun)
    async def wrapper(*args, **kwargs):
        start = time.time()

        result = await fun(*args, **kwargs)
        
        end = time.time()
        print(f"{fun.__name__} takes {end - start:.4f}s to finish")
        return result
        
    return wrapper

def logger(fun):
    @wraps(fun)
    async def wrapper(*args, **kwargs):

        now = datetime.datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{formatted_date} [LOG] calling {fun.__name__} | args: {kwargs}")

        result = await fun(*args, **kwargs)

        return result
    return wrapper