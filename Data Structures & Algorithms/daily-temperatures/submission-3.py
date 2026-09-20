class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 0

        # stack of temps with no warmer days found
        stack = []
        result = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while len(stack) != 0 and temp > temperatures[stack[-1]]:
                result[stack[-1]] = index - stack[-1]
                stack.pop()

            stack.append(index)

        return result