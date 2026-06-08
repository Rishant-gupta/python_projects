
import time
import datetime
import inspect
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
                        await asyncio.sleep(2)
        return wrapper
    return decorator




def timer(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        start = time.time()

        if asyncio.iscoroutinefunction(fun):
            async def asyncio_run():
                result = await fun(*args, **kwargs)
        
                end = time.time()
                print(f"{fun.__name__} took {end - start:.4f}s to finish")
                return result
            return asyncio_run()
        
        result = fun(*args, **kwargs)
        end = time.time()
        print(f"{fun.__name__} took {end - start:.4f}s to finish")
        return result

        
    return wrapper

def logger(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):

        now = datetime.datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{formatted_date} [LOG] calling {fun.__name__} | args: {kwargs}")

        if asyncio.iscoroutinefunction(fun):
            # it will only run of await obj.fetch() is called if await is not included then the async_run will not run and a small bug
            async def asyncio_run():
                result = await fun(*args, **kwargs)
                return result
            return asyncio_run()
        else:
            result = fun(*args, **kwargs)
            return result
    return wrapper