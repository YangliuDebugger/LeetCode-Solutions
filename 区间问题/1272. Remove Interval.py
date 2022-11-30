class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        # double pointer
        res = []
        for i, j in intervals:
            if j <= toBeRemoved[0] or i >= toBeRemoved[1]:
                res.append([i, j])
            else:
                if i < toBeRemoved[0]:
                    res.append([i, toBeRemoved[0]])
                if j > toBeRemoved[1]:
                    res.append([toBeRemoved[1], j])
        return res



