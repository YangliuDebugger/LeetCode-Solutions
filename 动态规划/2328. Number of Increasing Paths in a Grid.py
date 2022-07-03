class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        # 还是dp的题目
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for i in range(m)]
        N = 10 ** 9 + 7

        @cache
        def dfs(x, y):
            direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            dp[x][y] = 1
            for dx, dy in direction:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > grid[x][y]:
                    dp[x][y] += dfs(nx, ny)
            return dp[x][y] % N

        c = 0
        for i in range(m):
            for j in range(n):
                c = (c + dfs(i, j)) % N
        return c


