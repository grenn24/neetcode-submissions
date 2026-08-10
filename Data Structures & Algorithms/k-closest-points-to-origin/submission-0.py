import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        array = [(point[0] ** 2 + point[1] ** 2, point) for point in points]
        heapq.heapify(array)
        print(array)
        return [element[1] for element in heapq.nsmallest(k, array)]