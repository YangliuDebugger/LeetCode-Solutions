class Solution:
    @cache
    def canWin(self, currentState: str) -> bool:
        idx = 0
        can_win = True
        while idx < len(currentState) - 1:
            if currentState[idx:idx+2] == "++":
                # 只要有一种对手返回的时false就走那一种
                can_win &= self.canWin(currentState[:idx] + "--" + currentState[idx+2:])
            idx += 1
        return not can_win