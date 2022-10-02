class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        cnt = 0
        for i in range(1, min(a, b) +1):
            cnt += (a%i==0 and b%i==0)
        return cnt