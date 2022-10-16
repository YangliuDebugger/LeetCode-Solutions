class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 桶排序
        m, n = min(nums), max(nums)
        z = [0] * (n-m+1)
        for i in nums:
            z[i-m] += 1
        res = []
        for idx, i in enumerate(z):
            res.extend([idx+m]*i)
        return res