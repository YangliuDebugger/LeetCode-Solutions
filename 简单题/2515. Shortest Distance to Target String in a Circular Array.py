class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        d = collections.defaultdict(list)
        for idx, w in enumerate(words):
            d[w].append(idx)
        l = idx + 1
        if target not in d:
            return -1
        res = l
        for idx in d[target]:
            res = min(res, abs(idx - startIndex), l - abs(idx - startIndex))
        return res
