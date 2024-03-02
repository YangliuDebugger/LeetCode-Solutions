class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # greedy + double pointer
        s_target = set(target)
        s_source = set(source)
        if len(s_target - s_source) > 0:
            return -1

        simple_source = []
        for ch in source:
            if ch in s_target:
                simple_source.append(ch)

        t_idx = 0
        cnt = 0
        while True:
            cnt += 1
            for s_idx in range(len(simple_source)):
                if simple_source[s_idx] == target[t_idx]:
                    t_idx += 1
                    if t_idx == len(target):
                        return cnt


