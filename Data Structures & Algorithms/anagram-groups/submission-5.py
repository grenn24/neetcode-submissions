class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in result:
                result[sortedString].append(string)
            else:
                result[sortedString] = [string]
        
        return list(result.values())