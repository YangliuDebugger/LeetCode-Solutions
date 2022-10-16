class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        t = 1
        while n > 0:
            if n % 2 == 1:
                n -= 1
                powers.append(t)
            n //= 2
            t *= 2
        res = []
        N = 10 **9 + 7
        for s, e in queries:
            res.append(1)
            for i in range(s, e+1):
                res[-1] *= powers[i]
            res[-1] %= N
        return res