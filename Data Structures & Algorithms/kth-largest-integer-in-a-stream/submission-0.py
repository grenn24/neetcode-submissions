import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.numbers = [-x for x in nums]
        heapq.heapify(self.numbers)
        self.k = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.numbers, -val)
        return -heapq.nsmallest(self.k, self.numbers)[-1]
