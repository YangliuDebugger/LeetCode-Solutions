class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        a = bin(n)[2:][::-1]
        ans = [0, 0]
        for idx, i in enumerate(a):
            ans[idx%2] += int(i)
        return ans