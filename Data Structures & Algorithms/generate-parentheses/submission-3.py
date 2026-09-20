class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def helper(current, left, right):
            if left == right == n:
                result.append(current)
                return
            if left > n or right > n:
                return
            
            current += "("
            helper(current, left + 1, right)
            current = current[:-1]


            if right < left:
                current += ")"
                helper(current, left, right + 1)
                current = current[:-1]

        helper("", 0, 0)

        return result