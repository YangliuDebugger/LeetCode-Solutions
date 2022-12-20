class Solution:
    # simulation
    def smallestValue(self, n: int) -> int:
        def findPrime(x):
            s = 0
            left = 2
            while x >= left * left:
                while x % left == 0:
                    s += left
                    x //= left
                left += 1
            if x != 1:
                s += x
            return s
        x = n
        while True:
            y = findPrime(x)
            if x == y:
                return x
            x = y
