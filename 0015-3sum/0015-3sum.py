class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        res = []
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            j=i+1
            n=len(nums)-1
            target = -nums[i]

            while j<n:
                if j-1>i and nums[j]==nums[j-1]:
                    j+=1
                    continue
                if n+1<=len(nums)-1 and nums[n]==nums[n+1]:
                    n-=1
                    continue
                if nums[j]+nums[n]==target:
                    ans.append([-target, nums[j], nums[n]])
                    j+=1
                    n-=1
                elif nums[j]+nums[n] > target:
                    n-=1
                else: j+=1
        
        return ans