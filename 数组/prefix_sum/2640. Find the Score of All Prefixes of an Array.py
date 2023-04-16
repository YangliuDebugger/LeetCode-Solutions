class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        res = [0]
        curmax = nums[0]
        for i in nums:
            curmax = max(curmax, i)
            res.append(res[-1] + i + curmax)
        return res[1:]
