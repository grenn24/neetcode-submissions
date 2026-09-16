class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        if nums[right] > nums[left]:
            return nums[0]
        
        while left < right:
            mid = (left + right) // 2

            # mid is inside the lower portion
            if nums[mid] < nums[0]:
                right = mid
            else:
                left = mid + 1

        return nums[left]