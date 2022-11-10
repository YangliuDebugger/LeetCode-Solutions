class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        L1 = []
        L2 = []
        if len(s) != len(goal):
            return False
        for i, j in zip(s, goal):
            print(i, j)
            if i != j:
                L1.append(i)
                L2.append(j)
        if len(L1) == 0:
            return len(set(s)) < len(s)
        elif len(L1) == 2:
            return L1[0] == L2[1] and L1[1] == L2[0]
        return False