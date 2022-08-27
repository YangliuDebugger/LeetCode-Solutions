class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * (n - 2) for i in range(m - 2)]
        for i in range(m - 2):
            for j in range(n - 2):
                t = grid[i][j]
                for ii in range(i, i + 3):
                    for jj in range(j, j + 3):
                        t = max(t, grid[ii][jj])
                res[i][j] = t
        return res
