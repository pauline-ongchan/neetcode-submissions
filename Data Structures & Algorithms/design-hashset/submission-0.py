class MyHashSet:

    def __init__(self):
        self.temp = []
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.temp.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.temp.remove(key)
        
    def contains(self, key: int) -> bool:
        if not self.temp:
            return False
        for i in self.temp:
            if key == i:
                return True  
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)