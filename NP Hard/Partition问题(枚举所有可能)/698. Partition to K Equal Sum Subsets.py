class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        L = [0] * k
        nums.sort(reverse=True)
        ss = sum(nums)
        if ss % k != 0:
            return False
        target = ss // k
        self.find = False

        def enumerate(idx, fill_idx):
            if self.find:
                return
            if idx == len(nums):
                self.find = True
            else:
                for i in range(0, fill_idx + 1):
                    if L[i] + nums[idx] > target:
                        continue
                    L[i] += nums[idx]
                    if i == fill_idx and fill_idx < k - 1:
                        enumerate(idx + 1, fill_idx + 1)
                    else:
                        enumerate(idx + 1, fill_idx)
                    L[i] -= nums[idx]

        enumerate(0, 0)
        return self.find
