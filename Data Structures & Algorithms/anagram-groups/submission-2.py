class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            freqArray = [0] * 26
            for char in string:
                freqArray[ord(char) - ord('a')] += 1
            
            freqKey = ""
            for index, element in enumerate(freqArray):
                freqKey += chr(index + ord('a'))
                freqKey += str(element)

            if freqKey in result:
                result[freqKey] = result[freqKey] + [string]
            else:
                result[freqKey] = [string]
            
        return list(result.values())