import math
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        # a *b * c = gcd *LCM
        cnt = 0
        for i in range(len(nums)):
            gcd = nums[i]
            prod = nums[i]
            if nums[i] == k:
                cnt += 1
            for j in range(i + 1, len(nums)):
                if k % nums[j] != 0:
                    break
                if prod == k:
                    cnt += 1
                    continue
                if prod > k:
                    break
                gcd = math.gcd(gcd, nums[j])
                prod *= nums[j] // gcd
                if prod == k:
                    cnt += 1

        return cnt

