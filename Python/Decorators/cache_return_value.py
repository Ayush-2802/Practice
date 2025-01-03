import time


def cache(func):
    cache_v = {}
    print(cache_v)
    def internal(*args):
        if args in cache_v:
            return cache_v[args]
        res = func(*args)
        cache_v[args] = res
        return res
    return internal
        
@cache
def test(a,b):
    time.sleep(3)
    return (a+b)

print(test(2,3))
print(test(2,3))