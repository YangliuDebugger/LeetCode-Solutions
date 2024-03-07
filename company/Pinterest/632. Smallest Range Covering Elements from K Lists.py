class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        import heapq
        L = []
        cur_max = nums[0][0]

        for idx, l in enumerate(nums):
            L.append((l[0], idx, 0))
            cur_max = max(cur_max, l[0])
        heapq.heapify(L)
        self.res = [L[0][0], cur_max]
        self.len = cur_max - L[0][0]

        # print(self.res)
        # print(L)

        while True:
            val, list_idx, ele_idx = heapq.heappop(L)
            if cur_max - val < self.len:
                self.len = cur_max - val
                self.res = [val, cur_max]
            if ele_idx + 1 == len(nums[list_idx]):
                break
            # print(ele_idx, nums[list_idx])
            cur_max = max(cur_max, nums[list_idx][ele_idx + 1])
            heapq.heappush(L, (nums[list_idx][ele_idx + 1], list_idx, ele_idx + 1))

        return self.res