class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            
            # if latest temperature lower than current
            while len(stack) > 0 and temperatures[stack[-1]] < temp:

                    result[stack[-1]] = index - stack[-1]
                    stack.pop()

            stack.append(index)
            

                

        return result