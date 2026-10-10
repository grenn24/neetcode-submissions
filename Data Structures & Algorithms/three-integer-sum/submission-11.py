class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        print(nums)
        for i in range(len(nums) - 2):
            # skip duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            total = nums[left] + nums[right]
      
            prev = None
            while left < right:
                if total == -nums[i] and prev != [nums[left], nums[right]]:
                    result.append([nums[i], nums[left], nums[right]])
                    prev = [nums[left], nums[right]]
                    left += 1
                    total = nums[left] + nums[right]
                # total too positive
                elif total < -nums[i]:
                    left += 1
                    total = nums[left] + nums[right]
                else:
                    right -= 1
                    total = nums[left] + nums[right]
            
        return result