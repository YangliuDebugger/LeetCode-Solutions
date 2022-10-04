class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # O(nlogn)
        # 贪心， 从后往前，在分的尽可能少的情况下使得分的第一个数尽可能大
        cnt = 0
        n = len(nums)
        cur = nums[-1]
        for i in range(n - 2, -1, -1):
            if cur >= nums[i]:
                cur = nums[i]
                continue
            else:
                if nums[i] % cur == 0:
                    cnt += (nums[i] // cur - 1)
                else:
                    num_buckets = nums[i] // cur + 1
                    cnt += num_buckets - 1
                    cur = nums[i] // num_buckets
        return cnt

