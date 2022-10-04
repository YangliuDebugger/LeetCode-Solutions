class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        d = {}
        for idx, i in enumerate(nums):
            if i - idx not in d:
                d[i - idx] = 0
            d[i - idx] += 1
        n = len(nums)
        cnt = n * (n - 1) // 2
        for i in d:
            cnt -= d[i] * (d[i] - 1) // 2
        return cnt
