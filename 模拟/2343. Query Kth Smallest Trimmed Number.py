class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        res = []
        l = len(nums[0])
        for k, n in queries:
            r = [(num[l-n:], idx) for idx, num in enumerate(nums)]
            r.sort()
            res.append(r[k-1][1])
        return res