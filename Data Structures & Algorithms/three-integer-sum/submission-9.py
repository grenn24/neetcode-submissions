class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        result = []

        for index, num in enumerate(sortedNums):
            if index > 0 and sortedNums[index - 1] == sortedNums[index]:
                continue

            left = index + 1
            right = len(sortedNums) - 1
            target = -num
            while left < right:
                total = sortedNums[left] + sortedNums[right]

                if total == target:
                    if not (left > 0 and right < (len(sortedNums) - 1) and sortedNums[left - 1] == sortedNums[left] and sortedNums[right + 1] == sortedNums[right]):
                        result.append([num, sortedNums[left], sortedNums[right]])

                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                elif total > target:
                    right -= 1
            
        return result