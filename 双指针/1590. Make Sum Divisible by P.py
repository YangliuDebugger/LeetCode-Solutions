class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # 找到最短的subarray使得它和总的sum对p同余
        # 比如 [1,2,3,4,5,6] mod 5 余1，我们就要去找所有和余5mod1的子数组
        from collections import defaultdict
        ressum = [0] * (len(nums) + 1)
        d = defaultdict(list)
        d[0].append(-1)
        for idx, i in enumerate(nums):
            ressum[idx + 1] = (ressum[idx] + i) % p
            d[ressum[idx + 1]].append(idx)
        if ressum[-1] == 0:
            return 0

        best = len(nums)
        for end_mod in d:
            start_mod = (end_mod - ressum[-1] + p) % p
            if start_mod not in d:
                continue
            # 双指针扫描
            start_idx = 0
            end_idx = 0
            while start_idx < len(d[start_mod]) and end_idx < len(d[end_mod]):
                while start_idx < len(d[start_mod]) and d[start_mod][start_idx] < d[end_mod][end_idx]:
                    best = min(d[end_mod][end_idx] - d[start_mod][start_idx], best)
                    start_idx += 1
                end_idx += 1
        if best == len(nums):
            return -1
        return best
