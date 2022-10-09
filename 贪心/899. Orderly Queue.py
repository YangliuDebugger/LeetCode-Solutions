class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        ss = s
        if k == 1:
            for idx in range(len(s)):
                ss = min(ss, s[idx:] + s[:idx])
            return ss
        # 关键是理解 k >= 2 都可以通过同一种手法把这个string給sort了
        return ''.join(sorted(list(s)))
