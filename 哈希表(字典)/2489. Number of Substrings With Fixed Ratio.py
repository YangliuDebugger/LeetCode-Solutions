class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        # let's first consider special case, count substring with equal 0's and 1's, we use hash table to tackle this problem
        # for this general case, we may still apply similar logic
        d = collections.defaultdict(int)
        cnt = 0
        acc = 0
        d[0] = 1 # initialize
        for i in s:
            if i == '0':
                acc += num2
            else:
                acc -= num1
            cnt += d[acc]
            d[acc] += 1
        return cnt