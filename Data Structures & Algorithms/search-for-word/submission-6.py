class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[-1])


        
        def helper(path: List[tuple[int]], row: int, col: int):
            if (row, col) in path:
                return False

            if row < 0 or row > n - 1 or col < 0 or col > m - 1:
                return False


            new_path = path + [(row, col)]

            if len(new_path) > len(word):
                return False

            current_word = "".join([board[coord[0]][coord[1]] for coord in new_path])

            if current_word == word:
                return True


            return helper(new_path, row + 1, col) or helper(new_path, row - 1, col) or helper(new_path, row, col + 1) or helper(new_path, row, col - 1)

            

            

        for row in range(n):
            for col in range(m):
                result = helper([], row, col)
                if result:
                    return True

        return False