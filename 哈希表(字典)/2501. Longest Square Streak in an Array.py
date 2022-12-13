class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        t = set(nums)
        d = {}
        curent_max = -1
        for i in t:
            if i in d:
                continue
            cnt = 1
            ti = i * i
            while ti in t:
                if ti in d:
                    cnt += d[ti]
                    break
                ti *= ti
                cnt += 1
            if cnt >= 2:
                curent_max = max(curent_max, cnt)
            d[i] = cnt
        return curent_max
