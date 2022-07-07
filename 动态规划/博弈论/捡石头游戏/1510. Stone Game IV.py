class Solution(object):
    def winnerSquareGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        D = set()
        for i in range(1, int(n ** 0.5) + 1):
            D.add(i * i)

        @cache
        def Canwin(x):
            if x in D:
                return True
            else:
                for i in range(1, int(x ** 0.5) + 1):
                    if i * i <= x:
                        if not Canwin(x - i * i):
                            return True
                return False

        return Canwin(n)