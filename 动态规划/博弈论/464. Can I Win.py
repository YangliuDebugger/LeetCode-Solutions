class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 还是dp问题，状态空间为 2 ^ maxChoosableInteger (10 ^ 6)
        if desiredTotal > (1 + maxChoosableInteger) * maxChoosableInteger // 2:
            return False

        # 这个是下面的dp没有办法处理的
        if desiredTotal == 0:
            return True

        @cache
        def dp(total, n):
            if total <= 0:
                return False
            cnt = 1
            base = 1
            HeCanWin = True
            while n >= base and HeCanWin:  # prune
                t = n & base
                if t > 0:
                    HeCanWin &= dp(total - cnt, n ^ base)
                base = base << 1
                cnt += 1
            return not HeCanWin

        return dp(desiredTotal, 2 ** maxChoosableInteger - 1)
