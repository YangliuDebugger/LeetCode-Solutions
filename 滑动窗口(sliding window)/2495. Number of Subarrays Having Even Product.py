class Solution:
    def evenProduct(self, nums: List[int]) -> int:
        # how many subarray has at least one even number
        # we can find each subarray with only odd number
        n = len(nums)
        total = (1 + n) * n // 2
        start_idx = 0
        end_idx = 0
        while start_idx < n:
            while start_idx < n and nums[start_idx] % 2 == 0:
                start_idx += 1
            end_idx = start_idx
            while end_idx < n and nums[end_idx] % 2 == 1:
                end_idx += 1
            print(start_idx, end_idx)
            t = end_idx - start_idx
            total -= (1 + t) * t // 2
            start_idx = end_idx
        return total