class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # 还是一个botton up的dp 问题
        dp = [0] * 26
        for i in s:
            mid = ord(i) - 97
            start, end = max(mid-k, 0), min(mid+k, 25)
            # print(i, mid, start, end)
            dp[mid] += 1
            for j in range(start, end+1):
                if j == mid:
                    continue
                dp[mid] = max(dp[mid], dp[j]+1)
            # print(mid, dp)
        return max(dp)