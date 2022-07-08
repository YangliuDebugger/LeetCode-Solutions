class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        # 一维dp
        dp = [1, 0, 1]
        idx = 1
        N = len(obstacles) - 1
        Max = 10 ** 9
        while idx != N:
            # 横向走
            dp_0 = dp[:]
            if obstacles[idx] != 0:
                dp_0[obstacles[idx] - 1] = Max
            # 纵向走
            dp_1 = dp_0[:]
            dp_1[0] = min(dp_0[0], dp_0[1] + 1, dp_0[2] + 1)
            dp_1[1] = min(dp_0[0] + 1, dp_0[1], dp_0[2] + 1)
            dp_1[2] = min(dp_0[0] + 1, dp_0[1] + 1, dp_0[2])
            if obstacles[idx] != 0:
                dp_1[obstacles[idx] - 1] = Max

            dp = dp_1
            idx += 1
        print(dp)
        return min(dp)
    