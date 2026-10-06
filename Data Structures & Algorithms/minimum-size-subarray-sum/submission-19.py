class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        min_length = len(nums) + 1
        curr_sum = 0

        for end in range(len(nums)):
            curr_sum += nums[end]

            while curr_sum >= target:
                min_length = min(min_length, end - start + 1)
                curr_sum -= nums[start]
                start += 1
                

        return min_length if min_length != len(nums) + 1 else 0