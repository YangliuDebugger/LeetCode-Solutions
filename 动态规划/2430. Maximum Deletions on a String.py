class Solution:
    def deleteString(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        current_max = 0
        for i in range(len(s)-1,-1,-1):
            dp[i] = 1
            k = 1
            while i+2*k<len(dp):
                if s[i:i+k] == s[i+k:i+2*k]:
                    dp[i] = max(dp[i], 1+dp[i+k])
                    if dp[i] == current_max + 1:
                        break
                k+=1
            current_max = max(dp[i], current_max)
        # print(dp)
        return dp[0]