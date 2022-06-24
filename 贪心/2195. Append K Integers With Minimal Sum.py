class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        # 没有注意到nums中的数字可以不unique
        nums = list(set(nums))
        nums.sort()
        nums.append(10**10)
        cur_sum = 0
        # print(nums)
        for idx, i in enumerate(nums):
            # print(idx, i)
            if i - idx - 1 >= k:
                end_num = idx + k
                print(end_num)
                return (end_num + 1) * end_num // 2 - cur_sum
            cur_sum += i