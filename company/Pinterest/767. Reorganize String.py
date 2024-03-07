class Solution:
    def reorganizeString(self, s: str) -> str:
        import heapq
        d = {}
        for x in s:
            if x not in d:
                d[x] = 0
            d[x] += 1
        L = [(-d[k], k) for k in d]

        heapq.heapify(L)
        # print(L)
        res = ""
        hold = None
        while L:
            t, ch = heapq.heappop(L)
            res += ch
            if hold:
                heapq.heappush(L, hold)
            if t == -1:
                hold = None
            else:
                hold = (t + 1, ch)

        if hold:
            return ""
        return res

