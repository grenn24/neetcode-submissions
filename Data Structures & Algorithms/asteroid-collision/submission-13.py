class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        rightStack = []

        for index, asteroid in enumerate(asteroids):
            if asteroid < 0:
                isDestroyed = False
                while len(rightStack) > 0:
                    if rightStack[-1] < 0 and asteroid < 0:
                        break

                    if rightStack[-1] < 0 and asteroid > 0:
                        break

                    if abs(rightStack[-1]) > abs(asteroid):
                        isDestroyed = True
                        break
                    elif abs(rightStack[-1]) < abs(asteroid):
                        rightStack.pop()
                        continue
                    elif abs(asteroid) == abs(rightStack[-1]):
                        rightStack.pop()
                        isDestroyed = True
                        break
                    
                    break

                if not isDestroyed:
                    rightStack.append(asteroid)
                        
            else:
                rightStack.append(asteroid)

        
        return rightStack