class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()

        result = []

        index = 0
        while index < len(intervals):

            curr = intervals[index]

            if result and result[-1][1] >= curr[0]:
                result[-1][1] = max(result[-1][1], curr[1])

            else:
                result.append(curr)
            index += 1
            

        return result