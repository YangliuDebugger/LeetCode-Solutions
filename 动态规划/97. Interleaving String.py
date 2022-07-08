class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Dp 的问题 （复杂度 100 * 100 * 200）
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dp(idx1, idx2, idx3):
            if idx1 == len(s1) and idx2 == len(s2) and idx3 == len(s3):
                return True
            Can = False
            if idx1 < len(s1) and s1[idx1] == s3[idx3]:
                Can |= dp(idx1 + 1, idx2, idx3 + 1)
            if idx2 < len(s2) and s2[idx2] == s3[idx3]:
                Can |= dp(idx1, idx2 + 1, idx3 + 1)
            return Can

        return dp(0, 0, 0)