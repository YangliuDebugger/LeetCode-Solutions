class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # 用stack，记录别的函数用了多少时间
        from collections import defaultdict
        d = defaultdict(int)
        stack = []
        for log in logs:
            func, action, time = log.split(":")
            # print(func, action, time, stack)
            time = int(time)
            if action == 'start':
                if stack:
                    d[stack[-1][0]] = d[stack[-1][0]] + time - stack[-1][1]
                stack.append([func, time])
            else:
                d[stack[-1][0]] = d[stack[-1][0]] + time - stack[-1][1] + 1
                stack.pop()
                if stack:
                    stack[-1][1] = time + 1
        res = [d[str(i)] for i in range(n)]
        return res
