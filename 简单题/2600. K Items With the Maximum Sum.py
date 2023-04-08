class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        c = 0

        c += min(numOnes, k)
        k -= min(numOnes, k)
        k -= min(numZeros, k)
        c -= min(numNegOnes, k)

        return c