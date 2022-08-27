class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        t = [0] * len(edges)
        maxscore = -1
        maxidx = -1
        for idx, i in enumerate(edges):
            t[i] += idx
            if t[i] >= maxscore:
                if t[i] > maxscore:
                    maxscore = t[i]
                    maxidx = i
                else:
                    maxidx = min(maxidx, i)
        # print(t)
        return maxidx
