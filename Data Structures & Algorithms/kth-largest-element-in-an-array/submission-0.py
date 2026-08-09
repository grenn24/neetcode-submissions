import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        numbers = [-x for x in nums]
        heapq.heapify(numbers)

        return -heapq.nsmallest(k, numbers)[-1]