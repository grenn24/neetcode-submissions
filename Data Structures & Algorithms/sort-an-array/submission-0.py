class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        result = []

        leftIndex = 0
        rightIndex = 0

        while leftIndex < len(left) and rightIndex < len(right):
            if left[leftIndex] <= right[rightIndex]:
                result.append(left[leftIndex])
                leftIndex += 1
            else:
                result.append(right[rightIndex])
                rightIndex += 1


        result.extend(left[leftIndex:])
        result.extend(right[rightIndex:])

        return result