import threading
class LRUCache:
    '''Starting from Python 3.7, insertion order of Python dictionaries is guaranteed.'''
    def __init__(self, capacity: int):
        self.cache = {}
        self.lock = threading.Lock()
        self.size = 0
        self.capacity = capacity

    def get(self, key:int) -> int:
        '''
        :param key: (int) key
        :return: (int) value or -1
        '''
        with self.lock:
            if key in self.cache:
                val = self.cache[key]
                del self.cache[key]
                self.cache[key] = val
                return val
            else:
                return -1

    def put(self, key:int, value:int):
        with self.lock:
            if key in self.cache:
                del self.cache[key]
                self.cache[key] = value
            else:
                #if we need to evict the lru key
                if self.size == self.capacity:
                    cacheKeys = iter(self.cache)
                    del self.cache[next(cacheKeys)]
                    self.cache[key] = value
                else:
                    self.cache[key] = value
                    self.size += 1


def callAndReturn(operations, input):
    lru_cache = eval(f"{operations[0]}(*{input[0]})")
    res = [None]
    for op, inp in zip(operations[1:], input[1:]):
        res.append(eval(f"lru_cache.{op}(*{inp})"))
        print(lru_cache.cache)
    return res

operations = ['LRUCache','put','put','get','put','get','put','get','get','get']
input = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]


print(callAndReturn(operations, input))





