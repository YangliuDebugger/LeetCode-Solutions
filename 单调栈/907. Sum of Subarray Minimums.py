class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 从小往后扫，单调递增栈
        mono_stack = [[-999999999, -1]]
        N = 10 ** 9 + 7
        cnt = 0
        cur = 0
        for idx, v in enumerate(arr):
            if v >= mono_stack[-1][0]:
                cur += v
            else:
                while mono_stack[-1][0] >= v:
                    cur -= mono_stack[-1][0] * (mono_stack[-1][1] - mono_stack[-2][1])
                    mono_stack.pop()
                cur += v * (idx - mono_stack[-1][1])
            cnt += cur
            mono_stack.append([v, idx])
            cnt %= N
            cur %= N

        return cnt