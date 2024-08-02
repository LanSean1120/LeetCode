class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        num1 = sum(nums)
        Len = len(nums)
        
        nums += nums[:num1]
        count = sum(nums[:num1])
        ans = count
        for i in range(1, Len):
            if nums[i-1] == 1:
                count -=1
            if nums[i+num1-1] == 1:
                count+=1
            ans = max(ans, count)
        return num1 - ans


