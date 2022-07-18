class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d = {}
        import heapq
        for i in nums:
            t = sum([int(j) for j in list(str(i))])
            if t not in d:
                d[t] = []
            heapq.heappush(d[t], i)
            if len(d[t]) > 2:
                heapq.heappop(d[t])

        maxsum = -1
        for i in d:
            if len(d[i]) == 2:
                maxsum = max(maxsum, sum(d[i]))

        return maxsum