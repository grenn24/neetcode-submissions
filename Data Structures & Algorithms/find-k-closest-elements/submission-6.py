class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = sorted(arr)

        if k > len(arr):
            return []



        left = 0
        right = k - 1

        total_diff = 0

        for i in range(0, k):
            curr_diff = abs(arr[i] - x)
            total_diff += curr_diff

        for i in range(k, len(arr)):
            left_diff = abs(arr[left] - x)
            curr_diff = abs(arr[i] - x)

            new_total_diff = total_diff - left_diff + curr_diff

            if new_total_diff < total_diff:
                left += 1
                right += 1
            elif new_total_diff == total_diff and arr[left] >= arr[i]:
                left += 1
                right += 1
            else:
                break

        print(left, right)
        return arr[left: right + 1]


