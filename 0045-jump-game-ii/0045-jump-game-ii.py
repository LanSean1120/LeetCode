class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        nums = [nums[i] + i for i in range(len(nums))]
        count = 0
        longest = nums[0]
        last = 0
        while longest < len(nums)-1:
            temp = longest
            longest = max(nums[last:longest +1])
            last = temp
            count += 1
        return count+1
