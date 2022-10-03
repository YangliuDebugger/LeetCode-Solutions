class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        # 根据数据规模，至少是一个O(nlogn)的算法，比如快速排序，二分查找，堆
        # 分数公式定义这么怪，肯定是为了fit某个数据结构，算法
        # 其实就是一个sliding window里的max (用二叉树可以做， sortedList) 和 sum

        from sortedcontainers import SortedList

        n = len(chargeTimes)
        L = SortedList([0])
        start = 0
        end = 0
        running_sum = 0
        maxcnt = 0
        while start < n and end < n:
            while True:
                running_max = L[-1]
                if end < n and (running_sum + runningCosts[end]) * (end - start + 1) + max(running_max, chargeTimes[end]) <= budget:
                    running_sum += runningCosts[end]
                    L.add(chargeTimes[end])
                    end += 1
                else:
                    break
            maxcnt = max(maxcnt, end - start)

            # 移动start
            if start == end:
                start += 1
                end += 1
            else:
                running_sum -= runningCosts[start]
                L.remove(chargeTimes[start])
                start += 1
        return maxcnt


