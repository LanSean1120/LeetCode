class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if nums[0]<nums[-1] and nums[0]<nums[1]:
            return nums[0]
        if nums[-1]<nums[len(nums)-2] and nums[-1]<nums[0]:
            return nums[-1]
        start = 0
        end = len(nums)-1
        while start < end:
            if start - end == 1:
                return min(nums[start], nums[start+1])
            n = (start+end)//2
            if nums[n]<nums[n+1] and nums[n-1]>nums[n]:
                return nums[n]
            elif nums[n]<nums[start]:
                end = n
            elif nums[n]>nums[start]:
                start = n
        return nums[start]