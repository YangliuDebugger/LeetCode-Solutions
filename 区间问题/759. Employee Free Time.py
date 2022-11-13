"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        total_time = [s for p in schedule for s in p]
        total_time.sort(key=lambda x: x.start)
        res=[]
        current_start, current_end = total_time[0].start, total_time[0].end
        for t in total_time:
            if t.start > current_end:
                res.append(Interval(current_end, t.start))
                current_start, current_end = t.start, t.end
            else:
                current_end = max(current_end, t.end)
        return res

