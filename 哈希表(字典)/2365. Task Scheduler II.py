class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        # 模拟，需要每个task 的 cd
        d = {}
        total = 0
        for idx, i in enumerate(tasks):
            if i not in d:
                d[i] = total
                total += 1
            else:
                if total - d[i] > space:
                    d[i] = total
                    total += 1
                else:
                    d[i] = d[i] + space + 1
                    total = d[i] + 1
            # print(i, d[i])
        return total
