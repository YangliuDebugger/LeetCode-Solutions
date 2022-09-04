class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        t = 0
        MPG = [0, 0, 0]
        MPG_total = [0, 0, 0]
        for idx, trash in enumerate(garbage):
            for t in trash:
                if t == 'M':
                    MPG_total[0] += 1 + MPG[0]
                    MPG[0] = 0
                if t == 'P':
                    MPG_total[1] += 1 + MPG[1]
                    MPG[1] = 0
                if t == 'G':
                    MPG_total[2] += 1 + MPG[2]
                    MPG[2] = 0
            if idx < len(travel):
                for i in range(3):
                    MPG[i] += travel[idx]
        return sum(MPG_total)

