class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.path = ""
        self.leftOpen = 0
        self.rightOpen = 0

        def helper():
            if len(self.path) == n * 2:
                result.append(self.path)

            
            if self.leftOpen >= self.rightOpen and self.leftOpen < n:
                self.path += "("
                self.leftOpen += 1

                helper()

                self.path = self.path[:-1]
                self.leftOpen -= 1
            
            if self.leftOpen > self.rightOpen and self.rightOpen < n:
                self.path += ")"
                self.rightOpen += 1

                helper()

                self.path = self.path[:-1]
                self.rightOpen -= 1



            return

        
        helper()

        return result