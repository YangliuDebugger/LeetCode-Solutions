class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def cal_sum(i,j):
            return grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] + grid[i][j] + grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
        s = 0

        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                s = max(s, cal_sum(i,j))
        return s