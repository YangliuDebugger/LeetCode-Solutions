class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        z = [i+1 for i in aliceArrows]
        current_max = 0
        best_z = []
        for i in range(4096):
            t = list(bin(i)[2:][::-1])
            arrows = sum([int(i) * j for i, j in zip(t, z)])
            score = sum([idx for idx, i in enumerate(t) if i == '1'])
            if arrows <= numArrows and score > current_max:
                current_max = max(current_max, score)
                best_z = [int(i) * j for i, j in zip(t, z)]
                current_score = score
        best_z = best_z + [0] * (12 - len(best_z))
        best_z[0] += numArrows - sum(best_z)
        return best_z
