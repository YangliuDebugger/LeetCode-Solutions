class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        cnt = 0
        visit = set()
        for circle in circles:
            x, y, r = circle
            for xx in range(x, x-r-1, -1):
                for yy in range(y, y-r-1, -1):
                    if (x-xx)*(x-xx) + (y-yy)*(y-yy) <= r * r:
                        visit.add((xx, yy))
                        visit.add((2*x-xx, yy))
                        visit.add((xx, 2*y-yy))
                        visit.add((2*x-xx, 2*y-yy))
                    else:
                        break
        return len(visit)