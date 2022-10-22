class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        # dp 的题目：状态划分为，前n个，用了m个coupon，maxAmount为K的时候可以获得的最大的taste
        # 本质上还是0-1背包
        n = len(price)
        dp = [[[0] * (maxCoupons + 1) for i in range(maxAmount + 1)] for j in range(n + 1)]

        for i in range(n):
            for j in range(maxAmount + 1):
                for k in range(maxCoupons + 1):
                    # initialization

                    # if j > 0:
                    #    dp[i+1][j][k] = dp[i+1][j-1][k]
                    # 初始化不能用j-1而是用i是因为我们需要保证钱一定要够，dp[i][j][k]相当于不买

                    dp[i + 1][j][k] = dp[i][j][k]
                    # don't use coupon
                    if j >= price[i]:
                        dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j - price[i]][k] + tastiness[i])
                    # use coupon
                    if k >= 1 and j >= price[i] // 2:
                        dp[i + 1][j][k] = max(dp[i][j][k], dp[i][j - price[i] // 2][k - 1] + tastiness[i])
        return dp[n][maxAmount][maxCoupons]