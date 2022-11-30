class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        d = collections.defaultdict(int)
        mat = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                d[f"row_{i}"] += grid[i][j] * 2 - 1
                d[f"col_{j}"] += grid[i][j] * 2 - 1

        for i in range(m):
            for j in range(n):
                mat[i][j] = d[f"row_{i}"] + d[f"col_{j}"]
        return mat