class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d = {}
        res = []
        for i in nums:
            if i not in d:
                d[i] = -1
            d[i] += 1
            if d[i] == len(res):
                res.append([])
            res[d[i]].append(i)
        return res