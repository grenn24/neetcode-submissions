class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for str in strs:
            sortedStr = "".join(sorted(str))
            if sortedStr in result:
                result[sortedStr].append(str)
            else:
                result[sortedStr] = [str]

        return list(result.values())