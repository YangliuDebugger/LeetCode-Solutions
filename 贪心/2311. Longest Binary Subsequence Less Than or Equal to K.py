class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # 数据规模才1000, 感觉可以greedy, 把1的位置加进来，一个一个算
        L = []
        for idx, i in enumerate(s):
            if i == '1':
                L.append(idx)
        P = len(s) - len(L)
        cur = 0
        for idx in L[::-1]:
            M = 2 ** (len(s) - idx -1)
            if cur + M <= k:
                cur += M
                P += 1
            else:
                break
        # print(cur)
        return P