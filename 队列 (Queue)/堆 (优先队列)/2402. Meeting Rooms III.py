class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # 堆排序, 先按结束时间排序，然后按照room index 排序
        import heapq
        L = [(0, i) for i in range(n)]
        heapq.heapify(L)
        meetings.sort()
        rcnt = [0] * (n)
        for meeting in meetings:
            while True:
                end_time, room_idx = heapq.heappop(L)
                if end_time >= meeting[0]:
                    heapq.heappush(L, (end_time + meeting[1] - meeting[0], room_idx))
                    rcnt[room_idx] += 1
                    break
                else:
                    heapq.heappush(L, (meeting[0], room_idx))

        # print(rcnt)
        x = max(rcnt)
        for idx, i in enumerate(rcnt):
            if x == i:
                return idx
