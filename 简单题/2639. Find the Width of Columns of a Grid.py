class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = [0] * n
        for i in range(m):
            for j in range(n):
                res[j] = max(res[j], len(str(grid[i][j])))
        return res