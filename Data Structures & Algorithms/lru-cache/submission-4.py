class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache=[]
        self.values={}

    def get(self, key: int) -> int:
        if key not in self.values:
            return -1
        self.cache.remove(key)
        self.cache.append(key)
        return self.values[key]

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.cache.remove(key)
        elif len(self.cache)==self.capacity:
            lru = self.cache.pop(0)
            del self.values[lru]
        self.cache.append(key)
        self.values[key] = value
