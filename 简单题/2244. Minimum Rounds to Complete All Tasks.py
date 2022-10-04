class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = {}
        for i in tasks:
            if i not in d:
                d[i] = 0
            d[i] += 1
        cnt = 0
        for i in d:
            if d[i] % 3 == 0:
                cnt += d[i] // 3
            elif d[i] %3 == 2:
                cnt += 1 + d[i] // 3
            else:
                if d[i] == 1:
                    return -1
                else:
                    cnt += 2 + (d[i] - 4) // 3
        return cnt