class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        # bsearch
        def valid(j):  # i is the smallest possible number in this array
            cnt = 0
            kk = k
            for i in nums:
                if kk < 0:
                    return -1
                if i <= j:
                    kk -= (j - i)
                    cnt += 1
            if kk < 0:
                return -1
            if kk < cnt:
                return 0
            return 1

        def bsearch(low, high):
            if high - low <= 1:
                if valid(low) == 0:
                    return low
                return high
            mid = (low + high) // 2
            t = valid(mid)
            if t == 1:
                return bsearch(mid + 1, high)
            if t == -1:
                return bsearch(low, mid - 1)
            return mid

        z = bsearch(0, k + max(nums))
        # print(z)
        prod = 1
        kk = k
        N = 10 ** 9 + 7
        for i in nums:
            if i < z:
                kk -= (z - i)
        for i in nums:
            if i > z:
                prod = (prod * i) % N
            else:
                if kk > 0:
                    prod = (prod * (z + 1)) % N
                    kk -= 1
                else:
                    prod = (prod * z) % N
        return prod
