class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sorted_d = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        result = []
        for index, key in enumerate(sorted_d.keys()):
            if index < (k):
                result.append(key)
        
        return result