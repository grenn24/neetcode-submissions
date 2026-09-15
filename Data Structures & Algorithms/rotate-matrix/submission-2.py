class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse
        for i in range(len(matrix)):
            for j in range(len(matrix[i]) // 2):
                matrix[i][j], matrix[i][len(matrix[i]) - j - 1] = matrix[i][len(matrix[i]) - j - 1], matrix[i][j]
