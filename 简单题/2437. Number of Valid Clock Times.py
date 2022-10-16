class Solution:
    def countTime(self, time: str) -> int:
        time = time[:2] + time[3:]

        def compare(a1, a2):
            for i in range(4):
                if a1[i] == '?' or a1[i] == a2[i]:
                    continue
                return False
            return True

        cnt = 0
        for i in range(2400):
            t = "{:04d}".format(i)
            s = int(t[2:])
            if s >= 60:
                continue
            if compare(time, t):
                cnt += 1
        return cnt