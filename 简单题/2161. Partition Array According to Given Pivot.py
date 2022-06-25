class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # 快速查找，快速排序的具体实现, 不inplace的话应该很容易，用双stack即可
        a = []
        b = []
        c = []
        for i in nums:
            if i < pivot:
                a.append(i)
            elif i == pivot:
                b.append(i)
            else:
                c.append(i)
        return a+b+c