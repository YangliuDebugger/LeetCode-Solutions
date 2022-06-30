from collections import defaultdict


class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        # hash
        import bisect
        ss = sum(nums)
        # print(ss)
        # 被替换的number在左半边还是右半边
        leftdiff = defaultdict(int)  # 被替换的number贡献给右半边
        rightdiff = defaultdict(int)  # 被替换的number贡献给左半边
        cursum = 0
        for idx, i in enumerate(nums[:len(nums) - 1]):
            cursum += i
            rightdiff[ss - cursum - cursum] += 1
        # initialization when no changing number
        global_max = rightdiff[0]

        cursum = 0
        for idx, i in enumerate(nums):
            # print(idx,i,leftdiff,rightdiff)
            rightcnt = rightdiff[k - i]
            leftcnt = leftdiff[i - k]
            cursum += i
            global_max = max(global_max, leftcnt + rightcnt)
            rightdiff[ss - cursum - cursum] -= 1
            leftdiff[ss - cursum - cursum] += 1

        return global_max

