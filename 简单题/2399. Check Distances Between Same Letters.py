class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d = {}
        for idx, i in enumerate(s):
            if i not in d:
                d[i] = []
                d[i].append(idx)
            else:
                l = ord(i) - ord('a')
                if distance[l] != idx - d[i][0] - 1:
                    return False
        return True