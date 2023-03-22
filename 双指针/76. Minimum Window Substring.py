# https://www.1point3acres.com/bbs/thread-957371-1-1.html

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding window
        d = {}
        current_total = len(t)
        for i in t:
            if i not in d:
                d[i] = 0
            d[i] += 1
        s_idx = 0
        e_idx = 0
        min_length = len(s) + 1
        min_s, min_e = -1, -1
        while s_idx < len(s):
            while e_idx < len(s) and current_total > 0:
                if s[e_idx] in d:
                    if d[s[e_idx]] > 0:
                        current_total -= 1
                    d[s[e_idx]] -= 1
                e_idx += 1
            # print(s_idx, e_idx, s[s_idx: e_idx], current_total, min_length, d)
            if current_total == 0:
                if min_length > e_idx - s_idx:
                    min_length = e_idx - s_idx
                    min_s, min_e = s_idx, e_idx
            else:
                break
            # move s_idx
            if s[s_idx] in d:
                d[s[s_idx]] += 1
                if d[s[s_idx]] > 0:
                    current_total += 1
            s_idx += 1

        if min_length == len(s) + 1:
            return ""
        return s[min_s: min_e]

