class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # x 必须和num2有相同的1
        cnt = bin(num2).count('1')
        z = ['0']*32 + list(bin(num1)[2:])
        res = [0] * len(z)
        for idx, v in enumerate(z):
            if cnt == 0:
                break
            if v == '1':
                res[idx] = 1
                cnt -= 1
        res = res[::-1]

        x = 1
        ans = 0
        for idx, v in enumerate(res):
            if v == 0:
                if cnt > 0:
                    ans += x
                    cnt -= 1
            else:
                ans += x
            x *= 2
        return ans