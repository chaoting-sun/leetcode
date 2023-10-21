class TimeMap:

    def __init__(self):
        self.keyToValue = defaultdict(list)
        self.keyToTime = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyToValue[key].append(value)
        self.keyToTime[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        values = self.keyToValue[key]
        times = self.keyToTime[key]
        if not values:
            return ""

        prev_id = self.binarySearch(times, timestamp)
        if prev_id == -1:
            return ""
        return values[prev_id]

    def binarySearch(self, times, target):
        l, r = 0, len(times) - 1
        while l <= r:
            c = l + (r - l) // 2
            if times[c] > target:
                r = c - 1
            elif times[c] < target:
                l = c + 1
            else:
                return c
        return l - 1



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)