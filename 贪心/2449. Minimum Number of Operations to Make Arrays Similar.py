class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        # O(n) huozhe O(nlogn)
        nums1 = []
        nums2 = []
        for i in nums:
            if i % 2 == 0:
                nums1.append(i)
            else:
                nums2.append(i)

        target1 = []
        target2 = []
        for i in target:
            if i % 2 == 0:
                target1.append(i)
            else:
                target2.append(i)

        nums1.sort()
        nums2.sort()
        target1.sort()
        target2.sort()

        z1 = [i - j for i, j in zip(nums1, target1)]
        z2 = [i - j for i, j in zip(nums2, target2)]
        cnt = 0
        for i in z1 + z2:
            if i > 0:
                cnt += i

        return cnt // 2