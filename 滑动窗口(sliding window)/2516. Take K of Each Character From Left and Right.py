class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        cnt = {'a': 0, 'b': 0, 'c': 0}
        for idx, c in enumerate(s):
            cnt[c] += 1
        if cnt['a'] < k or cnt['b'] < k or cnt['c'] < k:
            return -1

        # sliding window
        res = len(s)
        start_idx = 0
        end_idx = start_idx
        while start_idx < len(s):
            while end_idx < len(s):
                if cnt[s[end_idx]] > k:
                    cnt[s[end_idx]] -= 1
                    end_idx += 1
                else:
                    break
            res = min(res, len(s) - end_idx + start_idx)
            # this can tackle when start_idx == end_idx
            cnt[s[start_idx]] += 1
            start_idx += 1
        return res