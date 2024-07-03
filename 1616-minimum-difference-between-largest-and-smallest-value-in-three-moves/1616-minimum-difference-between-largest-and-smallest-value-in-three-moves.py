class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        candidate = []
        for i in range(4):
            candidate.append(nums[len(nums)-1-(3-i)]-nums[i])
        return min(candidate)