class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def helper(current, total, startIndex):
            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            for index in range(startIndex, len(candidates)):
                num = candidates[index]

                # skip to avoid creating duplicate branches
                if index > startIndex and candidates[index] == candidates[index - 1]:
                    continue

                current.append(num)
                helper(current, total + num, index + 1)
                current.pop()

        helper([], 0, 0)

        return result