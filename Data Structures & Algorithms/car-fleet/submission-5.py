class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        sortedCars = sorted(zip(position, speed), reverse=True, key=lambda x: x[0])

        for carPos, carSpeed in sortedCars:
            timeTaken = (target - carPos) / carSpeed
            
            if len(stack) == 0:
                stack.append(timeTaken)
                continue
            # car will travel slower than the previous fleet
            elif stack[-1] < timeTaken:
                stack.append(timeTaken)


        return len(stack)