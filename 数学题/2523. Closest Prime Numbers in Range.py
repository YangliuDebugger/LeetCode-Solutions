class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def rwh_primes1(n):
            # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
            """ Returns  a list of primes < n """
            sieve = [True] * (n // 2)
            for i in range(3, int(n ** 0.5) + 1, 2):
                if sieve[i // 2]:
                    sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
            return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]

        l = rwh_primes1(right + 1)
        cur_max = right - left + 10
        best = [-1, -1]
        for idx in range(1, len(l)):
            if l[idx - 1] < left:
                continue
            if l[idx] - l[idx - 1] < cur_max:
                cur_max = l[idx] - l[idx - 1]
                best = [l[idx - 1], l[idx]]
        return best