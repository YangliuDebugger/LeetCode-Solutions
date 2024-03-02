class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x)
        remove = 0
        end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] >= end:
                end = interval[1]
            else:
                remove += 1
                end = min(end, interval[1])
        return remove