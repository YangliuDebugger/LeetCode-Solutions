class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        names = [(idx, v) for idx, v in enumerate(names)]
        names.sort(key = lambda x: -heights[x[0]])
        return [v for idx, v in names]