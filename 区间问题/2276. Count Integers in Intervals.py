# 有点区间合并的题目 + 二分查找
# trick: list插入一个元素，替换一段元素的写法不同python运行效率不同

class CountIntervals:

    def __init__(self):
        self.Intervals = []  # always make sure there is no overlap in this list by merging intervals
        self.cnt = 0

    def bsearch(self, val, mode, low, high):
        if high - low <= 1:
            if mode == 'right':
                if val >= self.Intervals[high][0] - 1:
                    return high
                if val >= self.Intervals[low][0] - 1:
                    return low
                return low - 1
            else:
                if val <= self.Intervals[low][1] + 1:
                    return low
                if val <= self.Intervals[high][1] + 1:
                    return high
                return high + 1
        mid = (low + high) // 2
        if val < self.Intervals[mid][0]:
            return self.bsearch(val, mode, low, mid)
        if val > self.Intervals[mid][1]:
            return self.bsearch(val, mode, mid, high)
        return mid

    def add(self, left: int, right: int) -> None:
        if not self.Intervals:
            self.Intervals.append([left, right])
            self.cnt += right - left + 1
            return

        left_idx = self.bsearch(left, 'left', 0, len(self.Intervals) - 1)
        right_idx = self.bsearch(right, 'right', 0, len(self.Intervals) - 1)

        if left_idx > right_idx:  # doesn't overlap with any existed intervals
            # self.Intervals = self.Intervals[:left_idx] + [[left, right]] + self.Intervals[left_idx:]
            self.Intervals[left_idx:left_idx] = [[left, right]]  #
            self.cnt += right - left + 1
        else:  # merge intervals
            new_left, new_right = min(self.Intervals[left_idx][0], left), max(self.Intervals[right_idx][1], right)
            for idx in range(left_idx, right_idx + 1):
                self.cnt -= self.Intervals[idx][1] - self.Intervals[idx][0] + 1
                # self.Intervals = self.Intervals[:left_idx] + [[new_left, new_right]] + self.Intervals[right_idx+1:]
            self.Intervals[left_idx:right_idx + 1] = [[new_left, new_right]]
            self.cnt += new_right - new_left + 1

        # print(self.Intervals)

    def count(self) -> int:
        return self.cnt

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
