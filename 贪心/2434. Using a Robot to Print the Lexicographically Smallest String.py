# The greedy strategy works as following:
# If the last char of t is less or equal to all remaining chars of s, we will pop this char into p
class Solution:
    def robotWithString(self, s: str) -> str:
        # 记录该字符最后一次出现时的位置
        d = {}
        for idx, i in enumerate(s):
            d[i] = idx
        L = sorted([i for i in d.keys()])
        current = 0
        stack = []  # robot
        res = []
        s_idx = 0
        while s_idx < len(s):
            i = s[s_idx]
            if i != L[current]:
                stack.append(i)
                s_idx += 1
                continue
            # i == L[current]
            res.append(i)
            if s_idx == d[i]:
                while current < len(L) and d[L[current]] <= s_idx:
                    current += 1
            s_idx += 1

            if current == len(L):
                break

            while stack and stack[-1] <= L[current]:
                res.append(stack.pop())

        return ''.join(res + stack[::-1])