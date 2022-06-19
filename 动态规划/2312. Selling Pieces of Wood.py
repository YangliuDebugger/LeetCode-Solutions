# 这道题的take away就是，bottom up有时会比top down要快，取决重复计算是否intensive
# 第二点就是记忆化搜索的时候，二维数组的读取是要比map要快的
# 第三点是要灵活使用@cache，可以省去显式更新memory的操作
class Solution:
    def sellingWood_My(self, m: int, n: int, prices: List[List[int]]) -> int:
        # 8415ms
        # DP 递推
        # D = {}
        D = [[None] * (n + 1) for _ in range(m + 1)]
        K = {(i, j): k for i, j, k in prices}

        def dp(m, n):
            if D[m][n] is not None:
                return D[m][n]
            D[m][n] = 0
            if (m, n) in K:
                D[m][n] = K[(m, n)]
            # 横切
            for i in range(1, m // 2 + 1):
                D[m][n] = max(D[m][n], dp(i, n) + dp(m - i, n))
            # 纵切
            for i in range(1, n // 2 + 1):
                D[m][n] = max(D[m][n], dp(m, i) + dp(m, n - i))
            return D[m][n]

        return dp(m, n)

    def sellingWood_bottomup(self, m, n, prices):
        # 6060 ms
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for w, h, p in prices:
            dp[w][h] = p
        for w in range(1, m + 1):
            for h in range(1, n + 1):
                for a in range(1, w // 2 + 1):
                    dp[w][h] = max(dp[w][h], dp[a][h] + dp[w - a][h])
                for a in range(1, h // 2 + 1):
                    dp[w][h] = max(dp[w][h], dp[w][a] + dp[w][h - a])
        return dp[m][n]

    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        # top down dp
        p = [[0] * (n + 1) for _ in range(m + 1)]
        for x, y, z in prices: p[x][y] = z

        @cache
        def f(i, j):
            if i == 0 or j == 0: return 0
            ans = p[i][j]
            for ii in range(1, i // 2 + 1):
                ans = max(ans, f(ii, j) + f(i - ii, j))
            for jj in range(1, j // 2 + 1):
                ans = max(ans, f(i, jj) + f(i, j - jj))
            return ans

        return f(m, n)