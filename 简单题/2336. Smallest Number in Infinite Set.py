class SmallestInfiniteSet:

    def __init__(self):
        self.p = set([i for i in range(1, 1005)])

    def popSmallest(self) -> int:
        t = min(self.p)
        self.p.remove(t)
        return t

    def addBack(self, num: int) -> None:
        self.p.add(num)