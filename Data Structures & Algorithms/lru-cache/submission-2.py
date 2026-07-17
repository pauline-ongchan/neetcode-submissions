class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.used = []

    def get(self, key: int) -> int:
        if key in self.cache:
            self.used.remove(key)
            self.used.append(key)
            return self.cache[key]
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.cap:
                del self.cache[self.used[0]]
                del self.used[0]
            self.used.append(key)
        else:
            self.used.remove(key)
            self.used.append(key)

        self.cache[key] = value