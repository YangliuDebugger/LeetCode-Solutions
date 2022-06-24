class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        # dp的题，时间复杂度O(numLaps^2 + tires)
        N = len(tires)
        upper_bound = 10 ** 10
        min_time = [upper_bound] * (numLaps + 1)
        for x in tires:
            cur_time = x[0]
            factor = x[0]
            for i in range(min(30, numLaps)):
                if cur_time <= upper_bound:
                    min_time[i + 1] = min(min_time[i + 1], cur_time)
                    factor *= x[1]
                    cur_time += factor

        @cache
        def dp(n):
            if n == 1:
                return min_time[1]
            res = min_time[n]
            for i in range(1, n // 2 + 1):
                res = min(res, dp(i) + dp(n - i) + changeTime)
            return res

        return dp(numLaps)
