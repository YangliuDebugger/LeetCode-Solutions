class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        for i in range(30, 0, -1):
            if '0' * i + '1' * i in s:
                return i * 2
        return 0


