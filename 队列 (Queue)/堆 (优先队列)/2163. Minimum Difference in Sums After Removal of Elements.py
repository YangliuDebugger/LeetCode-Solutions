class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        import heapq
        cnt = 0
        left_min, right_max = [0] * (n + 1), [0] * (n + 1)
        left, right = [-i for i in nums[:n]], [i for i in nums[2 * n:]]
        heapq.heapify(left)
        heapq.heapify(right)
        left_min[0] = -sum(left)
        right_max[n] = sum(right)

        # 不断地去维护一个大小为n的大/小根堆
        for i in range(0, n):
            # print(left, nums[n+i])
            item = heapq.heappushpop(left, -nums[n + i])
            left_min[i + 1] = left_min[i] + item + nums[n + i]

        # print(left_min)

        opt = left_min[n] - right_max[n]
        for i in range(n - 1, -1, -1):
            # print(right, nums[n+i], right_max)
            item = heapq.heappushpop(right, nums[n + i])
            right_max[i] = right_max[i + 1] - item + nums[n + i]
            opt = min(left_min[i] - right_max[i], opt)

        # print(right_max)

        return opt