class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d = {}
        maxx = 0
        for i in range(len(nums)-1):
            if nums[i] == key:
                if nums[i+1] not in d:
                    d[nums[i+1]] = 0
                d[nums[i+1]] += 1
                maxx = max(maxx, d[nums[i+1]])
        print(d, maxx)
        for i in d:
            if d[i] == maxx:
                return i