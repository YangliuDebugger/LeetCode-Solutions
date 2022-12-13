class Allocator:

    def __init__(self, n: int):
        self.memory = [-1] * n

    def allocate(self, size: int, mID: int) -> int:
        start_idx = 0
        while start_idx < len(self.memory):
            while start_idx < len(self.memory) and self.memory[start_idx] != -1:
                start_idx += 1
            end_idx = start_idx
            while end_idx < len(self.memory) and self.memory[end_idx] == -1 and end_idx - start_idx < size:
                end_idx += 1
            if end_idx - start_idx == size:
                self.memory[start_idx:end_idx] = [mID] * size
                return start_idx
            start_idx = end_idx
        return -1

    def free(self, mID: int) -> int:
        cnt = 0
        for idx in range(len(self.memory)):
            if self.memory[idx] == mID:
                self.memory[idx] = -1
                cnt += 1
        return cnt

# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)