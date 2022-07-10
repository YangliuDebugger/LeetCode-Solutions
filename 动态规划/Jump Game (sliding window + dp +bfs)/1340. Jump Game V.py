class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # 会拐弯的最长下降子序列，数据规模才1000，够小
        # 当做dp问题来解, 用top-down dp for 写法上的便利
        @cache
        def dp(n):
            cur_max = 0
            best = 1
            for left_idx in range(n - 1, max(n - d, 0) - 1, -1):
                if arr[left_idx] >= arr[n]:
                    break
                best = max(best, 1 + dp(left_idx))

            for right_idx in range(n + 1, min(n + d + 1, len(arr))):
                if arr[right_idx] >= arr[n]:
                    break
                best = max(best, 1 + dp(right_idx))

            return best

        global_max = 0
        for i in range(len(arr)):
            global_max = max(global_max, dp(i))
            # print(i, dp(i))
        return global_max

