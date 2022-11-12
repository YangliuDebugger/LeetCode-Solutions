class Solution:
    def countOrders(self, n: int) -> int:
        # we need to make sure D always after P
        # 排列组合问题
        # 全排列 / 2 ^ n
        N = 10 **9 + 7
        cnt = 1
        t = n
        for i in range(1,2*n+1):
            # 这里可以优化成相邻的两个数之间必然有一个偶数
            while i % 2 == 0 and t > 0:
                i //= 2
                t -= 1
            cnt = cnt * i % N
        return cnt

