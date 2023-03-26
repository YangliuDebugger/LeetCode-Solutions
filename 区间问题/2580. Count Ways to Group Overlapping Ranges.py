class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        # UF?, build, merge interval
        ranges.sort()
        dis = 1
        last = ranges[0][1]
        for idx in range(1, len(ranges)):
            if last < ranges[idx][0]:
                dis += 1
            last = max(last, ranges[idx][1])
        return 2 ** dis % (10 ** 9 + 7)