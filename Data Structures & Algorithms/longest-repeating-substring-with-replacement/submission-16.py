class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        max_length = 0
        
        for right in range(len(s)):
            curr_char = s[right]
            

            if curr_char in freq:
                freq[curr_char] += 1
                
            else:
                freq[curr_char] = 1

            max_freq = list(sorted(freq.values()))[-1]
       

            number_of_replacements = right - left + 1 - max_freq

            while number_of_replacements > k:
                curr_char = s[left]
                freq[curr_char] -= 1
                max_freq = list(sorted(freq.values()))[-1]
                left += 1
                number_of_replacements = right - left + 1 - max_freq

            max_length = max(right - left + 1, max_length)


        return max_length

            