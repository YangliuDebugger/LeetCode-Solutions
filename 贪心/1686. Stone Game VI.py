class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        t = [[i-j,i,j] for i, j in zip(aliceValues, bobValues)]
        t.sort(key=lambda x:abs(x[0]), reverse=True)
        x1 = sum([x[1] for x in t[0::2]])
        x2 = sum([x[2] for x in t[1::2]])
        if x1 > x2:
            return 1
        elif x1 == x2:
            return 0
        return -1