class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def get_base_rep(k):
            a = n
            L = []
            while a > 0:
                L.append(a % n)
                a //= n
            return L == L[::-1]

        for i in range(n - 2, 1, -1):
            if not get_base_rep(i):
                return False
        return True
