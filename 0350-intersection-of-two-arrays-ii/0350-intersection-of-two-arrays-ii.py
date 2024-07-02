class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        if len(nums1)>len(nums2):
            return self.intersect(nums2, nums1)
        for elem in nums1:
            if elem in nums2:
                ans.append(elem)
                nums2.remove(elem)
        return ans
        