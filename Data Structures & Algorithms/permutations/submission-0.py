class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
     

        def helper(tmp: List[int], used: List[int]):
            if len(tmp) == len(nums):
                result.append(tmp)
            
            unused = list(filter(lambda x: x not in used, nums))
            if not unused:
                return
            else:
                for newElement in unused:
                    newTmp = tmp + [newElement]
                    newUsed = used + [newElement]
                    helper(newTmp, newUsed)


        helper([], [])

        return result



