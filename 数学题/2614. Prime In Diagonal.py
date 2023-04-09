class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(x):
            if x <= 1:
                return False
            for i in range(2, min(x, int(x ** 0.5 + 2))):
                if x % i == 0:
                    return False
            return True

        v = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j or i + j == len(nums) - 1:
                    if isPrime(nums[i][j]):
                        v = max(v, nums[i][j])
        return v