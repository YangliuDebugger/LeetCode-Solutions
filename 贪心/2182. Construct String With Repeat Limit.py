# takeaway: List的拼接操作远比list的append操作要费时很多。we should use list.append() rather than list + list
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # stack 可以解，贪心
        d = {}
        for i in s:
            if i not in d:
                d[i] = 0
            d[i] += 1
        L = [[i, d[i]] for i in d]
        L.sort()
        res = ["#"]
        while L:
            if res[-1][0] == L[-1][0]:
                if len(L) >= 2:
                    res.append(L[-2][0])
                    if L[-2][1] > 1:
                        L[-2][1] -= 1
                    else:
                        x = L.pop()
                        L.pop()
                        L.append(x)
                else:
                    break
            else:
                if L[-1][1] <= repeatLimit:
                    res.append(L[-1][0] * L[-1][1])
                    L.pop()
                else:
                    res.append(L[-1][0] * repeatLimit)
                    if L[-1][1] > repeatLimit:
                        L[-1][1] = L[-1][1] - repeatLimit
                    else:
                        L.pop()
        return ''.join(res)[1:]
