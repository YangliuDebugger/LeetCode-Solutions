class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        # basiacally we need to make a[i] == a[i+k]
        # mod question
        l = len(arr)
        visit = [0] * l
        L = []
        for idx, _ in enumerate(arr):
            if visit[idx] == 1:
                continue
            L.append([])
            ii = idx
            while visit[ii] == 0:
                visit[ii] = 1
                L[-1].append(arr[ii])
                ii = (ii + k) % l
        ss = 0
        for l in L:
            l.sort()
            # we can use quick select to get medium quickly
            medium = l[len(l)//2]
            for i in l:
                ss += abs(medium - i)
        return ss