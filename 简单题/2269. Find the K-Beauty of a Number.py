class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        t = str(num)
        N = len(t)
        cnt = 0
        for i in range(N - k + 1):
            if int(t[i:i + k]) == 0:
                continue
            if num % int(t[i:i + k]) == 0:
                cnt += 1
        return cnt
