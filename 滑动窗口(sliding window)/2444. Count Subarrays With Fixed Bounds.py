class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        cnt = 0
        left_minK_idx, left_maxK_idx = -1, -1
        good_idx = 0
        for idx, i in enumerate(nums):
            if minK <= i <= maxK:
                if i == minK:
                    left_minK_idx = idx
                if i == maxK:
                    left_maxK_idx = idx
                if left_minK_idx > -1 and left_maxK_idx > -1:
                    left_len = min(left_minK_idx, left_maxK_idx) - good_idx + 1
                    cnt += left_len
            else:
                left_minK_idx = -1
                left_maxK_idx = -1
                good_idx = idx + 1
        return cnt