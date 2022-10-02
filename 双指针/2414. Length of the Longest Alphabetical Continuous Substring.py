class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        # double pointer
        start, end = 0, 0
        L = [ord(i) for i in s]
        cnt = 0
        while start < len(s):
            end = start + 1
            while end < len(s) and L[end] == L[end-1]+1:
                end += 1
            cnt = max(cnt, end - start)
            start = end
        return cnt