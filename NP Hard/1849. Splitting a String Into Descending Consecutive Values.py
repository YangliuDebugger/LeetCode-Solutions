class Solution:
    def splitString(self, s: str) -> bool:
        # NP hard 问题
        @cache
        def dp(idx, next_val):
            if idx == len(s):
                return True
            # 这一个条件非常重要，用来对付 "200100"
            if next_val == 0 and int(s[idx:]) == 0:
                return True
            end = idx + 1
            while end <= len(s) and int(s[idx:end]) != next_val:
                end += 1
            if int(s[idx:end]) == next_val:
                return dp(end, next_val - 1)
            else:
                return False

        can = False
        for i in range(1, len(s)):
            can |= dp(i, int(s[:i]) - 1)

        return can
