class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        maxFreq = 0
        count = [0] * 26
        result = 0

        while right < len(s):
            # Update count
            idx = ord(s[right]) - ord('A')
            count[idx] += 1
            # Update maxFreq
            maxFreq = max(maxFreq, count[idx])
            
            while (right - left + 1) - maxFreq > k:
                # Update count
                idx = ord(s[left]) - ord('A')
                count[idx] -= 1

                left += 1

            result = max(result, right - left + 1)

            right += 1
        
        return result