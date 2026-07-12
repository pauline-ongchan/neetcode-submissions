class TimeMap:

    def __init__(self):
        self.TimeMap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key] = []
        self.TimeMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.TimeMap:
            return ""
        res = []
        timestamps = []
        res = self.TimeMap[key]
        for i in range(len(res)):
            timestamps.append(res[i][1])
        l = 0
        r = len(timestamps)
        index = -1
        while l < r:
            mid = (l + r) // 2
            if timestamp == timestamps[mid]:
                return res[mid][0]
            elif timestamp > timestamps[mid]:
                index = mid
                l = mid + 1
            else:
                r = mid 
        if index == -1:
            return ""
        return res[index][0]
                

        
