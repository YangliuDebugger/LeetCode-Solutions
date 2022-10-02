class Solution:
    def equalFrequency(self, word: str) -> bool:
        d = {}
        cnt = 0
        key = 0
        for w in word:
            if w not in d:
                d[w] = 0
            d[w] += 1
        l = sorted(d.values())

        t1, t2 = l[:], l[:]
        t1[-1] -= 1
        t2[0] -= 1

        t1 = set(t1)
        t2 = set(t2)
        t1.discard(0)
        t2.discard(0)

        return len(t1) == 1 or len(t2) == 1