class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        grid = [sorted(l) for l in grid]
        return sum([ max([grid[j][idx] for j in range(len(grid))]) for idx in range(len(grid[0]))])