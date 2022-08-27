import math


def binomial_cooefficient(n, k):
    n_fac = math.factorial(n)
    k_fac = math.factorial(k)
    n_minus_k_fac = math.factorial(n - k)
    return n_fac / (k_fac * n_minus_k_fac)


@cache
def pailie(n, k):
    n_fac = math.factorial(n)
    k_fac = math.factorial(n - k)
    return n_fac // k_fac


P = [10, 9 * 9, 9 * 9 * 8, 9 * 9 * 8 * 7, 9 * 9 * 8 * 7 * 6, 9 * 9 * 8 * 7 * 6 * 5, 9 * 9 * 8 * 7 * 6 * 5 * 4,
     9 * 9 * 8 * 7 * 6 * 5 * 4 * 3, 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2, 9 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2]


class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        t = [int(i) for i in str(n)]
        l = len(t)

        if l == 1:
            return n

        idx = 0
        count = 0
        for i in range(l - 1):
            count += P[i]

        visit = [0] * 10
        used = 0
        # print(count, t, l)
        while idx < l:
            if idx == 0:
                m = 1
            else:
                m = 0
            for i in range(m, 10):
                if visit[i] == 0:
                    if i < t[idx]:
                        count += pailie(9 - visit.count(1), l - 1 - idx)
                    else:
                        break
            if i > t[idx] or (i == t[idx] and visit[i] == 1):
                break

            visit[i] = 1
            idx += 1

        if len(set(t)) == l:
            count += 1

        return count - 1


