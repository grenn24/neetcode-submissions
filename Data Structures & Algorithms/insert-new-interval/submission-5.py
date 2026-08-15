class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        index = 0

        while (index < len(intervals) and intervals[index][1] < newInterval[0]):
            result.append(intervals[index])
            index += 1

        while (index < len(intervals) and intervals[index][0] <= newInterval[1]):
            newInterval[0] = min(intervals[index][0], newInterval[0])
            newInterval[1] = max(intervals[index][1], newInterval[1])
            index += 1

        result.append(newInterval)

        while (index < len(intervals) and intervals[index][0] > newInterval[1]):
            result.append(intervals[index])
            index += 1

        

        return result
