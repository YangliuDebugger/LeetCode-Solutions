class Solution:
    def coloredCells(self, n: int) -> int:
        # 数学题， 斜着看直接可以写出来
        return n * n + (n-1) * (n-1)