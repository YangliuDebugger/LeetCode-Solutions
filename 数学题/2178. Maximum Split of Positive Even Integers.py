class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        # 2 + 4 + ... + 2k = k(k+1)       (k+1)(k+2)
        if finalSum % 2 == 1:
            return []
        k = int(finalSum ** 0.5) - 2
        while k*(k+1) <= finalSum:
            k+=1
        T =  [2*i for i in range(1, k)]
        s = sum(T)
        if s == finalSum:
            return T
        T[-1] = T[-1] + (finalSum - s)
        return T