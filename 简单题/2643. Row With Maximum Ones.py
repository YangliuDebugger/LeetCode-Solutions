class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        t = [sum(x) for x in mat]
        f = max(t)
        return [t.index(f), f] # .index returns the first element