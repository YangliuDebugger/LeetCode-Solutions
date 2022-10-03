class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        # 数据规模这么小，甚至可以枚举了？
        import itertools
        m, n = len(matrix), len(matrix[0])
        L = [int(''.join([str(i) for i in s]), 2) for s in matrix]
        print(L)

        stuff = [1]
        for i in range(n - 1):
            stuff.append(stuff[-1] * 2)
        stuff = stuff[::-1]

        maxcnt = 0
        for subset in itertools.combinations(stuff, numSelect):
            z = sum(subset)
            cnt = 0
            for i in L:
                if i | z == z:
                    cnt += 1
            maxcnt = max(maxcnt, cnt)
        return maxcnt
