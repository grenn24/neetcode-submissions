class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 0 or len(s1) > len(s2):
            return False

        left = 0
        right = len(s1) - 1
        freqArrayS1 = [0] * 52
        freqArrayS2 = [0] * 52

        for index, char in enumerate(s1):
            idx1 = ord(char) - ord('a')
            idx2 = ord(s2[index]) - ord('a')
            freqArrayS1[idx1] += 1
            freqArrayS2[idx2] += 1

        while right < len(s2):

            if freqArrayS2 == freqArrayS1:
                
                return True



            freqArrayS2[ord(s2[left]) - ord('a')] -= 1
            left += 1
            right += 1
            if right < len(s2):
                freqArrayS2[ord(s2[right]) - ord('a')] += 1
        return False