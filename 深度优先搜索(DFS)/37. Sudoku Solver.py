class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = {i: set() for i in range(9)}
        col = {i: set() for i in range(9)}
        square = {i: set() for i in range(9)}

        q = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    q.append((i, j))
                else:
                    number = int(board[i][j])
                    row[i].add(number)
                    col[j].add(number)
                    square_row, square_col = i // 3, j // 3
                    square_idx = square_row * 3 + square_col
                    square[square_idx].add(number)

        self.find = False
        full = set([i for i in range(1, 10)])

        def dfs(idx):
            if idx == len(q):
                self.find = True
            if self.find:
                return
            i, j = q[idx]
            avalible = full - (row[i] | col[j] | square[i // 3 * 3 + j // 3])
            for element in avalible:
                if not self.find:
                    row[i].add(element)
                    col[j].add(element)
                    square[i // 3 * 3 + j // 3].add(element)
                    board[i][j] = str(element)
                    dfs(idx + 1)
                    row[i].remove(element)
                    col[j].remove(element)
                    square[i // 3 * 3 + j // 3].remove(element)

        dfs(0)

