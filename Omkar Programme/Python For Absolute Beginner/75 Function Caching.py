import time
from functools import lru_cache
@lru_cache(maxsize=3)       # store function in lru_cache last three calls
def some_work(n):
    time.sleep(n)        # somework function take time for n secs
    return n

if __name__ == '__main__':
    print("now running some time")
    some_work(2)                     # first time function take time to store
    some_work(1)                     # new value function take time
    some_work(3)                     # new value function take time
    some_work(2)                     # second time use stored function
    print("done... calling again")
    input()
    some_work(3)                     # second time use stored function
    print("called again")