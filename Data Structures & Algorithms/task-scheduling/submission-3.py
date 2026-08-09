class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqArray = [0] * 26

        for task in tasks:
            idx = ord(task) - ord('A')
            freqArray[idx] += 1

        reversedArray = sorted(freqArray)
        f_max = reversedArray[-1]
        f_max_count = len(list(filter(lambda x: x == f_max, freqArray)))
    
        return max(len(tasks), ((f_max - 1) * (n + 1)) + f_max_count)