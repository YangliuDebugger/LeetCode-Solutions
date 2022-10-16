class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d = set(nums)
        maxx = -1
        for i in nums:
            if i > 0 and -i in d:
                maxx = max(i, maxx)
        return maxx