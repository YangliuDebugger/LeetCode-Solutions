class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        # 引理，为了得到最优解，如果移除了x，那么所有小于等于x的也都需要移除
        # 排序即可
        total = sum(beans)
        n = len(beans)
        beans.sort()
        mincnt = total
        removed = 0
        for idx, i in enumerate(beans):
            mincnt = min(mincnt, total - (n - idx) * i)
        return mincnt
