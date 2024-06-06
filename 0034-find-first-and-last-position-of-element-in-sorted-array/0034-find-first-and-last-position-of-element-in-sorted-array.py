class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = []
        if target in nums:
            i=0
            j=len(nums)-1
            while nums[i] != target:
                i+=1
            while nums[j] != target:
                j-=1
            return [i, j]
                
        else: return [-1,-1]