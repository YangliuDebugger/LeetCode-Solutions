class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # dp 的题目， 需要realize 一点就是dp一定是一个非降的数组
        # sorted by end time
        jobs = [(s, e, p) for s, e, p in zip(startTime, endTime, profit)]
        jobs.sort(key=lambda x: (x[1], x[0], x[2]))
        dp = [0] * (len(jobs) + 1)

        def bsearch(low, high, val):
            if high - low <= 1:
                if jobs[high][1] <= val:
                    return high
                if jobs[low][1] <= val:
                    return low
                return -1
            mid = (low + high) // 2
            if jobs[mid][1] <= val:
                return bsearch(mid, high, val)
            return bsearch(low, mid, val)

        for i in range(len(jobs)):
            start_time, end_time, profit = jobs[i]
            dp[i + 1] = dp[i]  # initialization
            last_job_idx = bsearch(0, i, start_time)
            dp[i + 1] = max(dp[last_job_idx + 1] + profit, dp[i + 1])

        return dp[-1]


