class Solution:
    def captureForts(self, forts: List[int]) -> int:
        sett = False
        last_idx = -100
        last_value = -100
        m = 0
        for idx, i in enumerate(forts):
            if i == 0:
                continue
            if not sett:
                last_idx, last_value = idx, i
                sett = True
                continue
            if i == last_value:
                last_idx, last_value = idx, i
                continue
            m = max(m, abs(idx - last_idx - 1))
            last_idx, last_value = idx, i
        return m