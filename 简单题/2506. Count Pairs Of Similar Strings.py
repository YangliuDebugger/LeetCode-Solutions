class Solution:
    def similarPairs(self, words: List[str]) -> int:
        cnt = 0
        d = {}
        for i in range(len(words)):
            s = ''.join(set(words[i]))
            if s not in d:
                d[s] = 0
            d[s] += 1
            cnt += d[s] - 1
        return cnt
