class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        # greedy
        cnt = 0
        last = nums[0] - 1
        for idx, i in enumerate(nums):
            # print(cnt, last)
            if cnt % 2 == 0:
                last = i
                cnt += 1
            else:
                if i == last:
                    continue
                else:
                    cnt += 1
        if cnt % 2 != 0:
            cnt -= 1
        return len(nums) - cnt