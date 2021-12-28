class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Deterministically make nums1 always at least the shorter of two arrays
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # Define lengths of the two arrays
        m = len(nums1)
        n = len(nums2)
        # Pointers for each array
        start = 0
        end = m
        # x1 x2 x3 | x4 x5
        # y1 y2 | y3 y4
        # x2 < y3, y2 < x4 to satisfy optimal pivot condition
        # Use binary search on smaller array to find the optimal pivot point
        while start <= end:
            # Create initial pivot for both arrays
            pivNums1 = (start + end) // 2
            pivNums2 = (m + n + 1) // 2 - pivNums1
            # Handle edge cases for going out of bounds
            lNums1 = float(-inf) if pivNums1 == 0 else nums1[pivNums1 - 1]
            rNums1 = float(inf)  if pivNums1 == m else nums1[pivNums1]
            lNums2 = float(-inf) if pivNums2 == 0 else nums2[pivNums2 - 1]
            rNums2 = float(inf)  if pivNums2 == n else nums2[pivNums2]
            # Check if we satisfy the pivot condition
            # Once the pivot point is found then we can look at the points around
            # the pivot point to determine the median
            # If total length is odd than the median is the greater of the two left
            # of the pivot point
            # If the total length is even than the median the average of the greater of
            # left and least of the two points right of pivot point            
            if lNums1 <= rNums2 and lNums2 <= rNums1:
                if (m + n) % 2 == 0:
                    return (max(lNums1, lNums2) + min(rNums1, rNums2)) / 2
                else:
                    return max(lNums1, lNums2)
            elif lNums1 > rNums2:
                end = pivNums1 -1
            else:
                start = pivNums1 + 1