class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        # used[i] indicates whether nums[i] is in current path
        used = [False] * len(nums)
        path = []

        def helper():
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for index, num in enumerate(nums):
                if used[index]:
                    continue

                path.append(num)
                used[index] = True

                helper()

                path.pop()
                used[index] = False
                    
                    
            return


        helper()

        return result



