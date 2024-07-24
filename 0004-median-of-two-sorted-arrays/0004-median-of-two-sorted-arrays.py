class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1 = len(nums1)
        n2 = len(nums2)
        n = (n1 + n2)
        half = n//2

        left, right = 0, n1-1
        
        while True:
            mid1 = (left + right)//2 #4->1
            mid2 = half - mid1 - 2 #6 -> 2 5-1-2

            left1 = nums1[mid1] if mid1>=0 else float('-inf')
            right1 = nums1[mid1+1] if (mid1+1)<n1 else float('inf')
            left2 = nums2[mid2] if mid2>=0 else float('-inf')
            right2 = nums2[mid2+1] if (mid2+1)<n2 else float('inf')

            if left1 <= right2 and left2 <= right1:
                if n%2:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                right = mid1-1
            else:
                left = mid1+1
