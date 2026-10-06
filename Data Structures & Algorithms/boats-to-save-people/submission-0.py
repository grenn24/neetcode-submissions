class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)

        start = 0
        end = len(people) - 1
        result = 0

        while start <= end:
            
            if people[start] + people[end] > limit:
                result += 1
                end -= 1
            elif start == end:
                result += 1
                break
            else:
                result += 1
                end -= 1
                start += 1

        return result