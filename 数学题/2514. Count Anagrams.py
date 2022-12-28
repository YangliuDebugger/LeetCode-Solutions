class Solution:
    def countAnagrams_naive(self, s: str) -> int:
        # 排列组合问题

        N = 10 ** 9 + 7
        d = []

        def count(freq):
            # n! / (a1!a2!...an!)
            start = math.factorial(sum(freq))
            for f in freq:
                start //= math.factorial(f)
            return start

        t = 1
        from collections import Counter
        for w in s.split():
            t = t * count(list(Counter(w).values())) % N
        return t

    def countAnagrams(self, s: str) -> int:

        # 这其实是一道很好的数学题, 除法的同余怎么转化成乘法的
        # 本题的难点就是如果先计算 n!，然后再除a1!a2!...an!，最后再取模，会非常耗时，因为有高精度的数值计算
        # 考虑到除法不满足mod分配率，即 a/b % m != ((a%m) / (b%m)) % m
        # 因为 m 是prime number，那么根据费马小定理，必有 b^(m-1) % m = 1, 也就是 (b * b^(m-2)) % m == 1
        # 所以 (a / b) % m = (a/b)%m*(b * b^(m-2)) % m = (a * b^(m-2)) % m

        N = 10 ** 9 + 7
        M = len(s) + 1
        fact = [1] * M
        invfact = [1] * M

        for i in range(2, M):
            fact[i] = fact[i - 1] * i % N
            # invfact[i] = invfact[i-1] * pow(i, -1, N) % N # we can also use pow(i, N-2, N) here, python support negative exp

        # 这里可以优化成我们只用计算一次pow
        invfact[-1] = pow(fact[-1], -1, N)
        for i in range(M - 2, 1, -1):
            invfact[i] = invfact[i + 1] * (i + 1) % N

        t = 1
        from collections import Counter
        for w in s.split():
            l = Counter(w).values()
            t = t * fact[sum(l)]
            for f in l:
                t = t * invfact[f]
            t %= N
        return t









