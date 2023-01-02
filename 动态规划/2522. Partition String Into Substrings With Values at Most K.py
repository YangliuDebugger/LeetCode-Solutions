class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        # dp 的题目
        dp = [len(s)+1] * (len(s) + 1)
        dp[0] = 0
        for i in range(len(s)):
            j = i
            if int(s[i]) > k:
                return -1
            while j>=0:
                if int(s[j:i+1]) <= k:
                    dp[i+1] = min(dp[j]+1, dp[i+1])
                    j -= 1
                else:
                    break
        return dp[-1]