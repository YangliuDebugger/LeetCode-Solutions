class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 二分查找 O(nlogn)
        def validation(weight):
            cur = 0
            cnt = 1
            for i in weights:
                # 我们不用考虑i>weight的情况，因为weight最小也是max(weights)
                if cur + i <= weight:
                    cur += i
                else:
                    cur = i
                    cnt += 1
            return cnt <= days

        def bsearch(low, high):
            if high - low <= 1:
                if validation(low):
                    return low
                return high
            mid = (low + high) // 2
            if validation(mid):
                return bsearch(low, mid)
            return bsearch(mid, high)

        return bsearch(max(weights), sum(weights))



