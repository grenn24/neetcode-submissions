from collections import deque

class TimeMap:

    def __init__(self):
        self.store = {}


        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.store:
            timestamps = self.store[key]
            if timestamps[-1][0] <= timestamp:
                timestamps.append((timestamp, value))
            else:
                timestamps.appendLeft((timestamp, value))
        else:
            self.store[key] = deque([(timestamp, value)])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        timestamps = self.store[key]

        left = 0
        right = len(timestamps) - 1

        timestamp_prev = None

        while left <= right:
            mid = (left + right) // 2

            if timestamps[mid][0] < timestamp:
                timestamp_prev = timestamps[mid]

            if timestamps[mid][0] == timestamp:
                return timestamps[mid][1]
            elif timestamps[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1


        if timestamp_prev is not None:
            return timestamp_prev[1]
        else:
            return ""

        
