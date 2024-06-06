class Solution(object):
    def partitionDisjoint(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = [0 for i in range(len(nums))]
        right = [0 for i in range(len(nums))]
        left[0] = nums[0]
        right[-1] = nums[-1]
        for i in range(1, len(nums)):
            left[i] = max(left[i-1], nums[i])
        for i in range(len(nums)-2, -1, -1):
            right[i] = min(right[i+1], nums[i])

        for i in range(len(nums)):
            if left[i]<=right[i+1]:
                return i+1