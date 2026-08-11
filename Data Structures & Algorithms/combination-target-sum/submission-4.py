class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        
        def helper(path: List[int], start: int):
            current_target = 0
            for element in path:
                current_target += element

            if current_target == target:
                result.append(path)

            if current_target > target:
                return

            if start > len(nums) - 1:
                return
            
            for index in range(start, len(nums)):
                helper(path + [nums[index]], index)
               
                
            
        helper([], 0)

        return result