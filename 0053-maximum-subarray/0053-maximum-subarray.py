class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = []
        ans = nums[0]
        current = nums[0]
        for i in range(1, len(nums)):
            current = max(current+nums[i], nums[i])
            ans = max(ans, current)
        return ans

