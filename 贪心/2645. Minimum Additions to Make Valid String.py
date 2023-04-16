class Solution:
    def addMinimum(self, word: str) -> int:
        # greedy + stack
        stack = []
        cnt = 0
        for w in word:
            if stack and len(stack) < 3:
                if w > stack[-1]:
                    stack.append(w)
                else:
                    cnt += 3 - len(stack)
                    stack = [w]
            else:
                stack = [w]
        cnt += 3 - len(stack)
        return cnt
