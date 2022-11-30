class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # key words:
        # distinct integers in the array
        # numbers are only 1 to n
        # subarray not subsequence
        idx = nums.index(k)
        # check left and right statistics
        from collections import defaultdict

        d_left = defaultdict(int)
        d_right = defaultdict(int)
        cnt = 0
        left_idx, right_idx = idx, idx
        cnnt = 1
        while left_idx >= 0:
            if nums[left_idx] < k:
                cnnt += 1
            else:
                cnnt -= 1
            d_left[cnnt] += 1
            left_idx -= 1

        cnnt = 1
        while right_idx < len(nums):
            if nums[right_idx] > k:
                cnnt += 1
            else:
                cnnt -= 1
            d_right[cnnt] += 1
            right_idx += 1

        for key in d_left:
            cnt += d_left[key] * d_right[key]
            cnt += d_left[key] * d_right[key + 1]
        return cnt






