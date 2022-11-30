class Solution:
    def pivotInteger(self, n: int) -> int:
        ss = (1+n) * n // 2
        cursum = 0
        for x in range(1, n+1):
            cursum += x
            if cursum == ss:
                return x
            ss -= x
        return -1
