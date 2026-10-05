class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        if len(nums) == 1:
            return nums

        while k > 0:
            
            end = nums[-1]

            curr = len(nums) - 2
            while curr >= 0:
                nums[curr + 1] = nums[curr]
                curr -= 1

            nums[0] = end



            k -= 1

