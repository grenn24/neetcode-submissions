class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = []

        for interval in intervals:
            if not result:
                result.append(interval)
            else:
                prev_interval = result[-1]
                # check for overlap
                if interval[1] >= prev_interval[0] and interval[0] <= prev_interval[1]:
                    prev_interval[1] = max(prev_interval[1], interval[1])
                else:
                    result.append(interval)

        return result