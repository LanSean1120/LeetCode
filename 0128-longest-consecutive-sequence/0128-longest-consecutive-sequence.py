class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=list(set(nums))
        if nums==[]:
            return 0
        if len(nums)==1:
            return 1
        nums.sort()
        i=0
        M = max(nums)
        A = []
        nu=1
        
        while i<len(nums)-1:
            if nums[i+1]==nums[i]+1:
                nu+=1
            elif nums[i+1]==nums[i]:
                nu+=1
            else:
                nu=1
            A.append(nu)
            i+=1
        return max(A)



        