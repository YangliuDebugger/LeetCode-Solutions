class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = {}
        for value, weight in items1:
            d[value] = weight
        for value, weight in items2:
            if value not in d:
                d[value] = 0
            d[value] += weight
        L = [[v, d[v]] for v in d]
        L.sort()
        return L