class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # 数据规模很小， 全部枚举也就2^20
        nums.sort()
        L = defaultdict(int)
        self.cnt = 0

        def gen(idx, last):
            if idx == len(nums):
                self.cnt += 1
                return
            if L[nums[idx] - k] == 0:
                L[nums[idx]] += 1
                gen(idx + 1, nums[idx])
                L[nums[idx]] -= 1
            gen(idx + 1, last)

        gen(0, nums[0] - k - 1)
        return self.cnt - 1
