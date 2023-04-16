class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        # 从前往后推，从后往前的话因为可以最优减枝，应该更快
        import heapq
        heapq.heapify(buses)
        heapq.heapify(passengers)
        best_time = -1
        last_time = -1
        while buses:
            bus = heapq.heappop(buses)
            cnt = 0
            while cnt < capacity and passengers and passengers[0] <= bus:
                # 我把这个passengers[0] 踢掉
                if last_time != passengers[0] - 1:
                    best_time = passengers[0] - 1
                last_time = passengers[0]
                heapq.heappop(passengers)
                cnt += 1
            if cnt < capacity and last_time != bus:
                best_time = bus
        return best_time

