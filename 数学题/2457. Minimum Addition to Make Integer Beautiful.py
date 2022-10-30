class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        N = n
        n = [0] + [int(i) for i in str(n)]
        ss = sum(n)

        best_num = 1000000000000000000

        if ss <= target:
            return 0

        for idx, i in enumerate(n):
            # 从idx开始不一样
            if i < 9:
                res = n[:idx] + [n[idx] + 1] + [0] * (len(n) - idx - 1)
            s = sum(res)
            if s <= target:
                best_num = min(best_num, int(''.join([str(i) for i in res])))
            # print(best_num)
        return best_num - N