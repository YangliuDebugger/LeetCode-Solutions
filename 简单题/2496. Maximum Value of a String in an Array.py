class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        v = 0
        for i in strs:
            try:
                z = int(i)
            except:
                v = max(v, len(i))
            else:
                v = max(v, z)
        return v
