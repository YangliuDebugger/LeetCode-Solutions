class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        # 完全可以生成所有的回文数，然后乘起来看看
        cnt = 0
        left, right = int(left), int(right)
        for i in range(1, 100000):
            si = str(i)
            n1 = int(si + si[::-1])
            n2 = int(si[:-1] + si[::-1])
            # print(n1, n2)
            n1 = n1 ** 2
            n2 = n2 ** 2
            if left <= n1 <= right and str(n1) == str(n1)[::-1]:
                cnt += 1
            if left <= n2 <= right and str(n2) == str(n2)[::-1]:
                cnt += 1
        return cnt
