# 非常易错，交了6次才过，本身不难
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        s1 = [0]
        s2 = [0]

        cnt = 0
        p = num % 10

        if num == 0:
            return 0
        if num < k:
            return -1

        if k == 0:
            if num % 10 == 0:
                return 1
            return -1

        zz = k
        while zz % 10 != 0:
            zz += k

        if p == 0:
            if num >= zz:
                return zz // k
            else:
                return -1

        kk = k
        while kk not in s1 and p not in s1:
            cnt += 1
            s1.append(kk)
            s2.append(k * cnt)
            kk = (kk + k) % 10

        print(s1)
        print(s2)

        if p in s1 and num >= s2[-1]:
            return cnt
        else:
            return -1
