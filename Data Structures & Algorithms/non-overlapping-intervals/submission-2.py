class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        result = 0
        index = 1


        while index < len(intervals):
            prev_interval = intervals[index - 1]
            curr_interval = intervals[index]

            if curr_interval[0] < prev_interval[1]:
                result += 1
                intervals.pop(index)
            else:
                index += 1

        
        return result
