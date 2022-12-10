class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        s, t = sum(damage), max(damage)
        return s + 1 - min(armor, t)