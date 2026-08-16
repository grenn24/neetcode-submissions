class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []

        for num in nums:
            if len(tail) == 0:
                tail.append(num)
                continue
            
            left = 0
            right = len(tail)

            while left < right:
                mid = (left + right) // 2

                if tail[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left == len(tail):
                tail.append(num)
            else:
                tail[left] = num

        return len(tail)