class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        # 其实也是可以算出来的
        base = '1' + '0' * ((intLength - 1) // 2)
        maxbase = '9' * len(base)
        base, maxbase = int(base), int(maxbase)
        res = []
        for q in queries:
            x = (q - 1 + base)
            if x > maxbase:
                res.append(-1)
                continue
            if intLength % 2 == 0:
                res.append(str(x)+str(x)[::-1])
            else:
                res.append(str(x)+str(x)[::-1][1:])
        return res


    # def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
    #     # 按顺序generate就可以了
    #     res = []
    #     tmp = []
    #     large_range = [str(i) for i in range(10)]
    #     def generate(idx):
    #         if idx > (intLength - 1) // 2:
    #             if intLength % 2 == 0:
    #                 res.append(''.join(tmp + tmp[::-1]))
    #             else:
    #                 res.append(''.join(tmp + tmp[::-1][1:]))
    #         else:
    #             start = 0
    #             if idx == 0:
    #                 start = 1
    #             for i in large_range[start:]:
    #                 tmp.append(i)
    #                 generate(idx+1)
    #                 tmp.pop()
    #     generate(0)
    #     # print(res)
    #     ans = []
    #     for i in queries:
    #         i -= 1
    #         if i < len(res):
    #             ans.append(int(res[i]))
    #         else:
    #             ans.append(-1)
    #     return ans