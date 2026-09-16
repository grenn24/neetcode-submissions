import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            # discard portion including mid
            if self.timeTaken(piles, mid) > h:
                left = mid + 1
            else:
                right = mid

        return left

        
    
    def timeTaken(self, piles: List[int], rate: int):
        return sum(math.ceil(pile / rate) for pile in piles)