class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d = {}
        for row in grid:
            a = ','.join([str(i) for i in row])
            if a not in d:
                d[a] = 0
            d[a] += 1

        def rotate(x):
            list_of_tuples = list(zip(*x))[::-1]
            return [list(elem) for elem in list_of_tuples]

        c = rotate(rotate(rotate(grid)))
        c = [row[::-1] for row in c]

        cnt = 0
        for row in c:
            a = ','.join([str(i) for i in row])
            if a not in d:
                continue
            cnt += d[a]

        return cnt