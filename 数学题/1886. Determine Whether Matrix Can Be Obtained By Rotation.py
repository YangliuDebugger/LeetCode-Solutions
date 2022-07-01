# 旋转2D list in python
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(x):
            list_of_tuples = list(zip(*x))[::-1]
            return [list(elem) for elem in list_of_tuples]

        for i in range(4):
            print(mat, target)
            if mat == target:
                return True
            target = rotate(target)

        return False
