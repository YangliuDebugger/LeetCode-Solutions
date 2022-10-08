class Solution(object):
    def minTimeToType(self, word):
        """
        :type word: str
        :rtype: int
        """
        s = 'a'
        cnt = 0
        for c in word:
            cnt += min(abs(ord(c) - ord(s)), abs(ord(c) - ord(s) - 26), abs(ord(c) - ord(s) + 26)) + 1
            s = c
        return cnt