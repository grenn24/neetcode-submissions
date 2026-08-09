class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        result = -float('inf')

        while left < right:
            area = abs(min(heights[left], heights[right])) * (right - left)
            result = max(result, area)

            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1


        return result