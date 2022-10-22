class Solution:
    def closestFair(self, n: int) -> int:
        while True:
            N = str(n)
            if len(N) % 2 == 1:
                return int('1' + '0'*((len(N)+1)//2) + '1'*(len(N)//2))
            else:
                cnt = 0
                for i in N:
                    if int(i) % 2 == 1:
                        cnt += 1
                    else:
                        cnt -= 1
                if cnt == 0:
                    return n
                n += 1