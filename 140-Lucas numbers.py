import time
from functools import wraps, lru_cache

#decorator function 
def time_func(func):
    #wraps each Lucas number function call with time calculation of processing  
    @wraps(func)
    def wrapper(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        print(f'Calculation tooks: {end - start} seconds')
        return result

    return wrapper    

#finds Lucas numers, using memoization
@lru_cache(maxsize=None)
@time_func
def lucas(n):
    #avoids from wrong input
    if type(n) != int or n < 1:
        raise ValueError("n must be a positive integer number")

    if n==0:
        return 2
    if n==1:
        return 1
    return lucas(n-1) + lucas(n-2)


print(lucas(100))