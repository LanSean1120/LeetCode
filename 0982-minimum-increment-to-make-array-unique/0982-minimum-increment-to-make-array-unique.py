class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        mx = nums[0]-1
        i=0
        while i<len(nums):
            if nums[i]<=mx:
                ans += mx-nums[i]+1
                mx +=1
            else:
                mx = nums[i]
            i+=1

        return ans