class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def helper(current, startIndex):
            result.append(current.copy())

            for index in range(startIndex, len(nums)):
                num = nums[index]
                if num not in current:
                    current.append(num)
                    helper(current, index)
                    current.pop()

        helper([], 0)

        return result