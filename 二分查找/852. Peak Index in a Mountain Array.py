class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # bsearch
        def bsearch(low, high):
            mid = (low + high) // 2
            if arr[mid-1] < arr[mid] < arr[mid+1]:
                return bsearch(mid, high)
            if arr[mid-1] > arr[mid] > arr[mid+1]:
                return bsearch(low, mid)
            return mid
        return bsearch(0, len(arr)-1)