class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def factorize(x):
            i = 2
            t = set()
            while x >= i * i:
                if x % i == 0:
                    t.add(i)
                    while x % i == 0:
                        x //= i
                i += 1
            if x != 1:
                t.add(x)
            return t
        res = set()
        for num in nums:
            res |= factorize(num)
        return len(res)