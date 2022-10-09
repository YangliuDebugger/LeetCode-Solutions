class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        last_time = 0
        long_time = 0
        long_id = -1
        for idd, time in logs:
            if time - last_time >= long_time:
                if time - last_time == long_time:
                    long_id = min(long_id, idd)
                else:
                    long_id = idd
                    long_time = time - last_time
            last_time = time
        return long_id