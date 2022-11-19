class Robot:

    def __init__(self, width: int, height: int):
        # face direction
        # north, east, south, west：0,1,2,3
        self.width = width
        self.height = height
        self.directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.face = 1
        self.x = 0
        self.y = 0
        self.D = {0: 'North', 1: 'East', 2: 'South', 3: 'West'}
        self.call = False

    def step(self, num: int) -> None:
        # corner case
        if not self.call:
            self.face = 2
            self.call = True

        num = num % (2 * self.width + 2 * self.height - 4)

        while num > 0:

            newx, newy = self.x + num * self.directions[self.face][0], self.y + num * self.directions[self.face][1]
            if 0 <= newx < self.width and 0 <= newy < self.height:
                self.x, self.y = newx, newy
                break

            if newx < 0:
                newx = 0
            elif newx >= self.width:
                newx = self.width - 1

            if newy < 0:
                newy = 0
            elif newy >= self.height:
                newy = self.height - 1

            maxstep = abs(newx - self.x) + abs(self.y - newy)
            self.x, self.y = newx, newy
            num -= maxstep
            self.face = (self.face - 1) % 4

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.D[self.face]

# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()