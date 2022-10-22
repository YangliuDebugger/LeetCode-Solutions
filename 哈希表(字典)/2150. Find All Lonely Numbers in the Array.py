class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        d = collections.defaultdict(int)
        for i in nums:
            d[i] += 1
            d[i-1]+=0
            d[i+1]+=0
        res = []
        for i in d:
            if d[i] == 1 and d[i-1] + d[i+1] == 0:
                res.append(i)
        return res