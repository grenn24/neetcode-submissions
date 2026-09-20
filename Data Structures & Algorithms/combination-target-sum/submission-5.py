class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        
        def helper(current, total, startIndex):
            if total > target:
                return
            if total == target:
                result.append(current[:])
                return
            
            for index in range(startIndex, len(nums)):
                num = nums[index]
                current.append(num)
                helper(current, total + num, index)
                current.pop()

        for index in range(len(nums)):
            helper([nums[index]], nums[index], index)

        return result