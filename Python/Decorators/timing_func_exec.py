import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func (*args, **kwargs)
        end = time.time()
        print(f"Function:{func.__name__} \nTimeTaken: {end-start}")
        return res
    return wrapper

@timer
def sol(n):
    time.sleep(n)

sol(2)