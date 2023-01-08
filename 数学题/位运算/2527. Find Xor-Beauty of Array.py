class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        # 3个不同: (i,j,k) 和 (j,i,k) 异或后就是0，可以对项相消
        # 2个不同: (i,i,j) 和 (j,j,i) 异或后就是0，可以对项相消
        # (i,j,i) 和 (j,i,i) 对消 (j,i,j) 和 (i,j,j) 对消
        # 1 个不同: (i,i,i) = i
        a = 0
        for i in nums:
            a ^= i
        return a