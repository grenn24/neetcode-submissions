class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = float('-inf')
        best_sum_ending_at_pos = [float('-inf')] * len(nums)
        curr_sum = 0

        left = 0
        right = 0

        while right < len(nums):
            curr_value = nums[right]
            curr_sum += curr_value
            
            best_sum_ending_at_pos[right] = max(curr_sum, best_sum_ending_at_pos[right])
            best_sum = max(curr_sum, best_sum)

            # restart from curr val position

            if curr_value > best_sum_ending_at_pos[right]:
                left = right
                curr_sum = 0

                continue
            
            
            
            right += 1

        return best_sum




            

