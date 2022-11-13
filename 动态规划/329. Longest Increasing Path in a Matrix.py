from functools import cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # dp的题目
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for i in range(m)]

        @cache
        def get_path(i, j):
            dp[i][j] = 1
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], get_path(ni, nj) + 1)
            return dp[i][j]

        best = 1
        for i in range(m):
            for j in range(n):
                best = max(best, get_path(i, j))
        return best