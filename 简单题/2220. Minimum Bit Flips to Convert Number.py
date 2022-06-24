class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        print(bin(start ^ goal)[2:])
        return str(bin(start ^ goal)[2:]).count("1")