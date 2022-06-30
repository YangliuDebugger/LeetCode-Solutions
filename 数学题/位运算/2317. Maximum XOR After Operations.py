# 数学证明: https://leetcode.com/problems/maximum-xor-after-operations/discuss/2195929/JavaC%2B%2BPython-1-Line-Solution-OR-of-All-Elements
class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        # 6 AND (6 XOR 4) 操作的结果是仅保留6中4不是1那个位置上的1
        # 贪心
        cnt = [0] * 32
        n = len(nums)
        for num in nums:
            s = bin(num)[2:][::-1]
            for idx, c in enumerate(s):
                if c == '1':
                    cnt[idx] = 1
        factor = 1
        res = 0
        for i in range(32):
            res += factor * cnt[i]
            factor *= 2
        return res
