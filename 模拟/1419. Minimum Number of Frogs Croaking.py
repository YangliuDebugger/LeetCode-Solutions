class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        cnt = 0
        maxcnt = 0
        d = collections.defaultdict(int)
        m = {'c': 1, 'r': 2, 'o': 3, 'a': 4, 'k': 5}

        for i in croakOfFrogs:
            idx = m[i]
            d[idx] += 1
            if idx == 1:
                cnt += 1
            else:
                if d[idx-1] == 0:
                    return -1
                d[idx-1] -= 1
                if idx == 5:
                    cnt -= 1
                    d[idx] -=1
            maxcnt = max(maxcnt, cnt)
        # corner case
        if sum(d.values()) > 0:
            return -1
        return maxcnt
