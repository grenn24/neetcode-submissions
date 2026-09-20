class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26

        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        max_freq = max(freq)
        no_of_max_freq = len(list(filter(lambda v: v == max_freq, freq)))
        result = (max_freq - 1) * (n + 1) + no_of_max_freq

        return  len(tasks) if result < len(tasks) else result