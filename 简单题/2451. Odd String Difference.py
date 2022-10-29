class Solution:
    def oddString(self, words: List[str]) -> str:
        d = {}
        for w in words:
            t = ''.join([chr(ord(i) - ord(min(list(w)))) for i in w])
            if t not in d:
                d[t] = []
            d[t].append(w)
        for i in d:
            if len(d[i]) == 1:
                return d[i][0]
