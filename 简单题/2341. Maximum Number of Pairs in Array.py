class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        res = [0, 0]
        for key in d:
            if d[key] % 2 == 0:
                res[0] += d[key] // 2
            else:
                res[0] += d[key] // 2
                res[1] += 1
        return res
