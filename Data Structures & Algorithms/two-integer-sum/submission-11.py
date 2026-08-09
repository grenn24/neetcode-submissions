class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortedNums = sorted(enumerate(nums), key = lambda x: x[1])
        left = 0
        right = len(sortedNums) - 1
        result = []

        while left < right:
            total = sortedNums[left][1] + sortedNums[right][1]
            if total == target:
                return sorted([sortedNums[left][0], sortedNums[right][0]])
                left += 1
                right -= 1
            elif total > target:
                right -= 1
            elif total < target:
                left += 1
            

        return []