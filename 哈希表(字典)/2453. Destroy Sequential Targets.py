class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        # 同余问题
        d1 = {}
        d2 = {}
        maxx = 0
        maxi = -1
        for i in nums:
            t = i % space
            if t not in d1:
                d1[t] = 0
                d2[t] = i
            d1[t] += 1
            d2[t] = min(d2[t], i)

        for i in d1:
            if d1[i] > maxx:
                maxx = d1[i]
                maxi = d2[i]
            elif d1[i] == maxx:
                maxi = min(maxi, d2[i])

        return maxi