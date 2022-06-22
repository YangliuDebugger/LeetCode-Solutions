class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        D = {}
        maxcnt = 0
        maxname = ""
        for m, s in zip(messages, senders):
            cnt = len(m.split(' '))
            if s not in D:
                D[s] = 0
            D[s] += cnt
            if D[s] >= maxcnt:
                if D[s] > maxcnt:
                    maxname = s
                else:
                    maxname = max(maxname, s)
                maxcnt = D[s]
        return maxname

