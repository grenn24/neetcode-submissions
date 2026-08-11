class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        
        def helper(path: List[int], start: int):
            if len(path) > len(nums) or start >= len(nums):
                return

            newPath = path + [nums[start]]
            result.append(newPath)
            helper(newPath, start + 1)
            helper(path, start + 1)
                

            return


        helper([], 0)
        
        return result