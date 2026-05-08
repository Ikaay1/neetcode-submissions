class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map[key]
        left = 0
        right = len(values)-1

        while left <= right:
            mid = (left+right)//2

            if values[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        if right < 0:
            return ""
        
        return values[right][1]
        
