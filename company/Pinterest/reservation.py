
# open_time:9:00
# close_time: 21:00
# total capacity =

import heapq

def FindAvailableSlots(start_time, end_time, total_capacity, reservation, K):
    left = start_time
    cnt = total_capacity
    L = [[end_time, -total_capacity]]
    for s, e, num in reservation:
        L.append([s, -num])
        L.append([e, num])
    heapq.heapify(L)
    res = []
    while L:
        right, num = heapq.heappop(L)
        if left != right:
            res.append([left, right, cnt])
        cnt += num
        left = right
    return res

print(FindAvailableSlots("08:00", "21:00", 5, [["09:00", "10:00", 1], ["09:30", "10:00", 2]], 3))
