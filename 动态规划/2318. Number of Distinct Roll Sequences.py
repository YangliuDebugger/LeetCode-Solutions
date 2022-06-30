class Solution:
    def distinctSequences(self, n: int) -> int:

        N = 10 ** 9 + 7

        if n == 1:
            return 6
        if n == 2:
            return 22

        mutual_prime = set([(2, 4), (2, 6), (3, 6), (4, 2), (4, 6), (6, 2), (6, 3), (6, 4)])

        # 看起来就像个dp啊
        dp = [[0] * 7 for _ in range(7)]

        for i in range(1, 7):
            for j in range(1, 7):
                if i != j and (i, j) not in mutual_prime:
                    dp[i][j] = 1

        for _ in range(3, n + 1):
            dp_tmp = [[0] * 7 for _ in range(7)]
            for i in range(1, 7):
                for j in range(1, 7):
                    if i == j or (i, j) in mutual_prime:
                        continue
                    jj = i
                    for ii in range(1, 7):
                        if ii == jj or (ii, jj) in mutual_prime or ii == j:
                            continue
                        dp_tmp[i][j] += (dp[ii][jj]) % N
            dp = dp_tmp

        return sum(sum(dp, [])) % N