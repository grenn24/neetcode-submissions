class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbersSet = set()
        for num in nums:
            if num in numbersSet:
                return True
            numbersSet.add(num);
        
        return False