class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        heavy = (mass >= 100)
        bulky = (length == 10000 or width == 10000 or height == 10000 or length * width * height >= 10 ** 9)
        if heavy:
            if bulky:
                return "Both"
            return "Heavy"
        else:
            if bulky:
                return "Bulky"
            return "Neither"