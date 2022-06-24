class Solution:
    def minimumTime_heap(self, time: List[int], totalTrips: int) -> int:
        import heapq
        # heap 问题，每次挑最小的, 或者二分查找应该也行
        # 时间复杂度: O(mlogn)，提交会超时, 需要一定的优化
        L = [(t, t) for t in time]
        heapq.heapify(L)
        end_time, cnt = 0, 0
        while cnt < totalTrips:
            end_time, unit = heapq.heappop(L)
            heapq.heappush(L, (end_time + unit, unit))
            cnt += 1
        return end_time

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # 时间复杂度: O(n)
        def validation(total_time):
            cnt = 0
            for i in time:
                cnt += total_time // i
            return cnt >= totalTrips

        def bsearch(low, high):
            if high - low <= 1:
                if validation(low):
                    return low
                return high
            mid = (low + high) // 2
            valid = validation(mid)
            if valid:
                return bsearch(low, mid)
            return bsearch(mid, high)

        return bsearch(0, 10 ** 7 * 10 ** 7)
