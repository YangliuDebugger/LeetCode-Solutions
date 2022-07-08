class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        # 二进制的题目
        target = list(bin(target)[2:])
        cnt = 0
        while len(target) > 1:
            if target[-1] == '1':
                cnt += 1
                target[-1] = '0'
            else:
                if maxDoubles > 0:
                    cnt += 1
                    maxDoubles -= 1
                    target.pop()
                else:
                    return cnt + int(''.join(target), 2) - 1
        return cnt
