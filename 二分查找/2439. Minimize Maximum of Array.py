class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # 其实就是一个操作当前位加1，之后的某一位-1, 这个用在valid里面去判断是否合规
        # 可以用bsearch

        def valid(m):
            cnt = 0
            for i in nums:
                cnt += m - i
                if cnt < 0:
                    return False
            return True

        def bsearch(left, right):
            if right - left <= 1:
                if valid(right):
                    return right
                return left
            mid = (left + right) // 2
            if valid(mid):
                return bsearch(left, mid)
            return bsearch(mid, right)

        return bsearch(0, max(nums))










