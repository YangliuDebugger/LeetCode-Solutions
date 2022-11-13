class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        # dp的题目，截止到目前可以选择几个回文数
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(n):
            # 初始化为到上一个字符截止时最多有多少，因为dp一定是一个非降的数列
            dp[i + 1] = dp[i]
            for j in range(i + 1 - k, -1, -1):
            # 这个条件可以优化成 for j in range(i+1-k,max(i+1-k-2,-1),-1):
            # 我们只需要检查 k 和 k+1的就可以了
                # s[j] == s[i] 小trick来略微剪枝
                if s[j] == s[i] and s[j:i + 1] == s[j:i + 1][::-1]:
                    dp[i + 1] = max(dp[i + 1], dp[j] + 1)
                    break
        return dp[-1]


