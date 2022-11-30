class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # 典型的binary search
        def valid(x):
            return sum([(i - 1) // x + 1 for i in nums]) <= threshold

        def bsearch(low, high):
            if high - low <= 1:
                if valid(low):
                    return low
                return high
            mid = (low + high) // 2
            if valid(mid):
                return bsearch(low, mid)
            return bsearch(mid, high)

        return bsearch(1, max(nums))