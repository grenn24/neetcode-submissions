class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        left = 0
        right = 0
        count = [0] * 100
        maxLength = 0

        while right < len(s):
            idx1 = ord(s[right]) - ord('A')
            count[idx1] += 1

            while count[idx1] > 1:
                idx2 = ord(s[left]) - ord('A')
                count[idx2] -= 1

                left += 1

            maxLength = max(right - left + 1, maxLength)
            right += 1

        return maxLength