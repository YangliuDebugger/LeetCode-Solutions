class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        L = [0] * (n * n)
        for i in range(n):
            for j in range(n):
                L[grid[i][j]] = [i, j]
        x, y = -2, -1
        for i in range(n * n):
            cx, cy = L[i]
            dx, dy = x - cx, y - cy
            if abs(dx) + abs(dy) == 3 and abs(dx) * abs(dy) == 2:
                x, y = cx, cy
                continue
            return False
        return True
