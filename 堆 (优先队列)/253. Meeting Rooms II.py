# https://www.1point3acres.com/bbs/thread-952644-1-1.html

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        import heapq
        cnt = 0
        L = []
        for s, e in intervals:
            if not L:
                L.append(e)
            else:
                while L and s >= L[0]:
                    heapq.heappop(L)
                heapq.heappush(L, e)
            cnt = max(cnt, len(L))
        return cnt