class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # find a point to minimize # N on the left side, and # Y on the right side
        Ycount = customers.count('Y')
        Ncount = len(customers) - Ycount
        current_Y = 0
        current_N = 0

        best_idx = 0

        min_penalty = 10000000
        for idx, c in enumerate(customers):
            if Ycount - current_Y + current_N < min_penalty:
                min_penalty = Ycount - current_Y + current_N
                best_idx = idx
            if c == 'Y':
                current_Y += 1
            else:
                current_N += 1
        # corner case
        if Ycount - current_Y + current_N < min_penalty:
                min_penalty = Ycount - current_Y + current_N
                best_idx = idx+1
        return best_idx
