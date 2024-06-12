class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        while nums!=[] and nums[0]<=0:
            nums.pop(0)
        nums = list(set(nums))
        nums.sort()
        i= 1
        while i<=len(nums) and i == nums[i-1]:
            i+=1
        return i
