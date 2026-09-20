class Solution:


    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(current):
            if len(current) == len(nums):
                result.append(current[:])
            for num in nums:
                if num not in current:
                    current.append(num)
                    helper(current)
                    current.pop()

        
        helper([])

        return result
  