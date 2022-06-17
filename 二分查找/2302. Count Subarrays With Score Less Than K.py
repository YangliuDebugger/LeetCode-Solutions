# 本来是O(n) sliding window的题目硬生生做成了O(NlogN)的二分查找

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 这道题还是predix_sum下面的bsearch, 复杂度为O(nlogn)
        N = len(nums)
        prefix_sum = [0] * (N + 1)
        for idx in range(len(nums)):
            prefix_sum[idx + 1] = prefix_sum[idx] + nums[idx]

        # for each start idx, use bsearch to find and point

        def calulate(idx0, idx1):  # [idx0, idx1]
            return (prefix_sum[idx1 + 1] - prefix_sum[idx0]) * (idx1 + 1 - idx0)

        def find_endidx(idx0, low, high):
            if high - low <= 1:
                if calulate(idx0, high) < k:
                    return high
                else:
                    return low
            mid = (high + low) // 2
            if calulate(idx0, mid) < k:
                return find_endidx(idx0, mid, high)
            else:
                return find_endidx(idx, low, mid)

        res = 0
        for idx in range(N):
            if nums[idx] >= k:
                continue
            end_idx = find_endidx(idx, idx, N - 1)
            res += (end_idx + 1 - idx)
        return res
