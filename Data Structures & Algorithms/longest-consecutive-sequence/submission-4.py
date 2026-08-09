class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums))

        if len(nums) == 0:
            return 0

        pointer1 = 0
        pointer2 = 0

        result = 1
        print(sorted_nums)
        for index, num in enumerate(sorted_nums):
            print(pointer1)
            print(pointer2)
            if pointer2 != pointer1:
                result = max(pointer2 - pointer1 + 1, result)
            
            if index == len(sorted_nums) - 1:
                continue
            
            if (sorted_nums[index + 1] == sorted_nums[index] + 1):
                pointer2 = index + 1

            if not (sorted_nums[index + 1] == sorted_nums[index] + 1):
                pointer2 = index + 1
                pointer1 = index + 1
        
        return result