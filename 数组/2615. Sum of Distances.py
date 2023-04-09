class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        d = {}
        for idx, i in enumerate(nums):
            if i not in d:
                d[i] = []
            d[i].append(idx)

        for i in d:
            s = sum(d[i]) - d[i][0] * len(d[i])
            res[d[i][0]] = s
            for jdx, j in enumerate(d[i]):
                if jdx == 0:
                    continue
                s = s + (2 * jdx - len(d[i])) * (j - d[i][jdx - 1])
                res[j] = s
        return res