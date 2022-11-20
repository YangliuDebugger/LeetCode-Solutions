class Solution:
    def countCollisions(self, directions: str) -> int:
        # scan from left to right
        right = 0
        stop = 0
        cnt = 0
        for i in directions:
            if i == 'S':
                if right > 0:
                    cnt += right
                    right = 0
                stop = 1
            elif i == 'R':
                right += 1
            else:
                if right > 0:
                    cnt += 2
                    cnt += right - 1
                    right, stop = 0, 1
                else:
                    if stop == 1:
                        cnt += 1
        return cnt
