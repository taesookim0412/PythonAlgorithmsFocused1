import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key]
            del self.cache[key]
            self.cache[key] = val
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        else:
            self.size += 1
        self.cache[key] = value
        # or len(self.cache)
        if self.size > self.capacity:
            self.size -= 1
            # or delkey = next(iter(self.cache))
            for key in self.cache.keys():
                del self.cache[key]
                return