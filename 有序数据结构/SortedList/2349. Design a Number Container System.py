from sortedcontainers import SortedList
from collections import defaultdict


class NumberContainers:

    def __init__(self):
        self.index2number = defaultdict(lambda: -1)
        self.num2index = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        ori_number = self.index2number[index]
        self.num2index[ori_number].discard(index)
        self.index2number[index] = number
        self.num2index[number].add(index)

    def find(self, number: int) -> int:
        if not self.num2index[number]:
            return -1
        return self.num2index[number][0]

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)