class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0
        for w in words:
            if w.startswith(pref):
                cnt += 1
        return cnt
