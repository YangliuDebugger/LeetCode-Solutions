class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # double pointer
        s1_idx = 0
        s2_idx = 0

        slots1.sort()
        slots2.sort()

        while s1_idx < len(slots1) and s2_idx < len(slots2):
            while s1_idx < len(slots1) and slots1[s1_idx][1] - max(slots2[s2_idx][0], slots1[s1_idx][0]) < duration:
                s1_idx += 1
            if s1_idx == len(slots1):
                return []

            while s2_idx < len(slots2) and slots2[s2_idx][1] - max(slots1[s1_idx][0], slots2[s2_idx][0]) < duration:
                s2_idx += 1
            if s2_idx == len(slots2):
                return []

            if slots1[s1_idx][1] - slots2[s2_idx][0] >= duration:
                x = max(slots1[s1_idx][0], slots2[s2_idx][0])
                return [x, x + duration]

        return []