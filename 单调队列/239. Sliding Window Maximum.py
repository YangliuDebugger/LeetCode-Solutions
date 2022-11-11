class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        res = []
        if k == 1:
            res.append(nums[0])  # for k=1 case
        q = deque([0])
        for i in range(1, len(nums)):
            if q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            if i >= k - 1:
                res.append(nums[q[0]])
        return res
