
class Solution:
    def reverseCountAndSay(self, numString):
        mem = {}
        def splitAndMerge(start, end):
            if start == end:
                return {}
            if (start, end) in mem:
                return mem[(start, end)]
            # recursive
            resutls = set() # to reduce potential duplicate from different split method
            if numString[start] != '0':
                resutls.add(numString[end] * int(numString[start:end]))

            for mid in range(start+1, end-1):
                result1 = splitAndMerge(start, mid)
                if len(result1) > 0:
                    result2 = splitAndMerge(mid+1, end)
                    if len(result2) > 0:
                        for str1 in result1:
                            for str2 in result2:
                                resutls.add(str1+str2)
            print(start, end, resutls)
            mem[(start, end)] = resutls
            return mem[(start, end)]

        return splitAndMerge(0, len(numString) - 1)


solution = Solution()
print(solution.reverseCountAndSay("111111"))