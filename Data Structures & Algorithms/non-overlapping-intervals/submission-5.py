class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        count = 0

        index = 1

        while index < len(intervals):
            prev = intervals[index - 1]
            curr = intervals[index]

            if prev[1] > curr[0]:
                intervals.pop(index)
                count += 1
                continue
            
            index += 1

        return count