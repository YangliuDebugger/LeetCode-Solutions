class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        import heapq
        t = [-i for i in nums]
        heapq.heapify(t)
        score = 0
        while k > 0:
            score -= t[0]
            heapq.heapreplace(t, -math.ceil(-t[0]/3))
            k -= 1
        return score
