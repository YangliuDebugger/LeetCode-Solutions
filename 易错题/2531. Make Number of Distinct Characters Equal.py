class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        d1 = {}
        d2 = {}

        def countWord(word, d):
            for c in word:
                if c not in d:
                    d[c] = 0
                d[c] += 1

        countWord(word1, d1)
        countWord(word2, d2)

        c1, c2 = len(d1), len(d2)
        # print(d1, d2)
        for i in "abcdefghijklmnopqrstuvwxyz":
            for j in "abcdefghijklmnopqrstuvwxyz":
                if i in d1 and j in d2:
                    if i == j:
                        if c1 == c2:
                            return True
                        continue
                    t1, t2 = c1, c2
                    if d1[i] == 1:
                        t1 -= 1
                    if d2[j] == 1:
                        t2 -= 1
                    if j not in d1:
                        t1 += 1
                    if i not in d2:
                        t2 += 1
                    if t1 == t2:
                        # print(t1, t2, i, j)
                        return True
        return False
