class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # bsearch 问题，每次从大的数切下那么多就好，ball必须是整数

        def Valid(x):
            cut = 0
            for i in nums:
                cut += (i - 1) // x
            return cut <= maxOperations

        def bsearch(low, high):
            if high - low <= 1:
                if Valid(low):
                    return low
                return high
            mid = (low + high) // 2
            if Valid(mid):
                return bsearch(low, mid)
            return bsearch(mid, high)

        return bsearch(1, max(nums))