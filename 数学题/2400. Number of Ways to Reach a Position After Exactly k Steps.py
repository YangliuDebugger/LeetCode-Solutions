class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        # 排列组合
        diff = abs(endPos - startPos)
        if diff % 2 != k % 2:
            return 0
        if k < diff:
            return 0
        # k = a + b = k
        # diff =a - b = diff
        a, b = (k + diff) // 2, (k - diff) // 2
        # k choose a
        # print(a,b)
        if a < b:
            a, b = b, a
        t = [i for i in range(a + 1, k + 1)]
        s = [i for i in range(1, b + 1)]

        # print(t, s)

        start = 1
        while len(t) > 0:
            while s and start % s[-1] == 0:
                start //= s[-1]
                s.pop()
            start *= t[-1]
            t.pop()

        while s and start % s[-1] == 0:
            start //= s[-1]
            s.pop()

        return start % (10 ** 9 + 7)