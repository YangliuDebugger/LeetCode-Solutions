class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        # 贪心就完事了
        mi, ma = min(nums), max(nums)

        mi_idx = None
        ma_idx = 0
        for idx, i in enumerate(nums):
            if i == mi and mi_idx is None:
                mi_idx = idx
            if i == ma:
                ma_idx = idx
        x = mi_idx + len(nums) - 1 - ma_idx
        if mi_idx > ma_idx:
            x -= 1
        return x
