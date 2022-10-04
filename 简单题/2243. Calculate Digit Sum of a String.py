class Solution:
    def digitSum(self, s: str, k: int) -> str:
        s = [int(i) for i in s]
        while len(s) > k:
            t = [sum(s[i:i+k]) for i in range(0, len(s), k)]
            t = ''.join([str(i) for i in t])
            s = [int(i) for i in t]
        return ''.join([str(i) for i in s])