class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        L = []
        m = len(matrix)
        n = len(matrix[0])
        s = 0
        posminx = 100000000
        negmaxx = -100000000
        negcnt = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] > 0:
                    s += matrix[i][j]
                    posminx = min(matrix[i][j], posminx)
                else:
                    s -= matrix[i][j]
                    negmaxx = max(negmaxx, matrix[i][j])
                    negcnt += 1
        if negcnt % 2 == 0:
            return s
        else:
            return s - 2 * min(posminx, abs(negmaxx))