class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # bsearch + sliding window
        nums.sort()

        def valid(diff):
            last = -1000000000000000
            cnt = 0
            # 大概脑测了一下，排序后从前往后找一定是最优策略的一种
            for i in nums:
                if i - last <= diff:
                    cnt += 1
                    last = -1000000000000000
                else:
                    last = i
            return cnt >= p

        low = 0
        high = nums[-1] - nums[0]
        while high - low >= 2:
            mid = (low + high) // 2
            if valid(mid):
                high = mid
            else:
                low = mid

        if valid(low):
            return low
        return high