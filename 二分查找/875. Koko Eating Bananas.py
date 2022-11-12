class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        def validation(x):
            cnt = 0
            for i in piles:
                cnt += (i // x + 1)
                if i % x == 0:
                    cnt -= 1
            return cnt <= h

        def bsearch(low, high):
            if high - low <= 1:
                if validation(low):
                    return low
                return high
            mid = (low + high) // 2
            if validation(mid):
                return bsearch(low, mid)
            return bsearch(mid, high)

        return bsearch(1, max(piles))



