class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # greedy就可以解决
        degree = [0] * n
        for s, e in roads:
            degree[s] += 1
            degree[e] += 1
        degree.sort()
        return sum([(idx + 1) * v for idx, v in enumerate(degree)])
