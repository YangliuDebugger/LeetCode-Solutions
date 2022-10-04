class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        # 选一个L形，with most 0's
        m, n = len(grid), len(grid[0])
        twos = [[0] * n for _ in range(m)]
        fives = [[0] * n for _ in range(m)]
        cul_two_row = [[0] * (n + 1) for _ in range(m + 1)]
        cul_five_row = [[0] * (n + 1) for _ in range(m + 1)]
        cul_two_col = [[0] * (n + 1) for _ in range(m + 1)]
        cul_five_col = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                t = grid[i][j]
                while t % 2 == 0:
                    twos[i][j] += 1
                    t //= 2
                while t % 5 == 0:
                    fives[i][j] += 1
                    t //= 5
                cul_two_row[i + 1][j + 1] = cul_two_row[i + 1][j] + twos[i][j]
                cul_five_row[i + 1][j + 1] = cul_five_row[i + 1][j] + fives[i][j]

        for j in range(n):
            for i in range(m):
                cul_two_col[i + 1][j + 1] = cul_two_col[i][j + 1] + twos[i][j]
                cul_five_col[i + 1][j + 1] = cul_five_col[i][j + 1] + fives[i][j]

        #         print(twos)
        #         print(fives)

        #         print (cul_two_row)
        #         print (cul_five_row)
        #         print (cul_two_col)
        #         print (cul_five_col)

        t = 0
        # 枚举拐点
        for i in range(m):
            for j in range(n):
                # 计算四个方向L的值

                left_two = cul_two_row[i + 1][j + 1] - cul_two_row[i + 1][0] - twos[i][j]
                left_five = cul_five_row[i + 1][j + 1] - cul_five_row[i + 1][0] - fives[i][j]

                up_two = cul_two_col[i + 1][j + 1] - cul_two_col[0][j + 1] - twos[i][j]
                up_five = cul_five_col[i + 1][j + 1] - cul_five_col[0][j + 1] - fives[i][j]

                right_two = cul_two_row[i + 1][-1] - cul_two_row[i + 1][j + 1]
                right_five = cul_five_row[i + 1][-1] - cul_five_row[i + 1][j + 1]

                down_two = cul_two_col[-1][j + 1] - cul_two_col[i + 1][j + 1]
                down_five = cul_five_col[-1][j + 1] - cul_five_col[i + 1][j + 1]

                maxx = max(min(left_two + up_two + twos[i][j], left_five + up_five + fives[i][j]),
                           min(left_two + down_two + twos[i][j], left_five + down_five + fives[i][j]),
                           min(right_two + up_two + twos[i][j], right_five + up_five + fives[i][j]),
                           min(right_two + down_two + twos[i][j], right_five + down_five + fives[i][j]))

                # if i==0 and j == 0:
                #     print(left_two, left_five, right_two, right_five)
                #     print(up_two, up_five, down_two, down_five)

                if maxx >= t:
                    # print(i, j, maxx)
                    t = max(t, maxx)
        return t



