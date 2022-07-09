class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # 堆 (优先队列)，每次选最大边际收益的来提高
        # 边际收益计算公式为 a+1/b+1 - a/b = (b-a) / (b(b+1))
        import heapq
        L = []
        for a, b in classes:
            heapq.heappush(L, [(a-b)/(b*b+b),a,b])
        while extraStudents > 0:
            _, a, b = heapq.heappop(L)
            extraStudents -= 1
            a, b = a+1, b+1
            heapq.heappush(L, [(a-b)/(b*b+b),a,b])
        return sum([a/b for _,a,b in L])/len(L)