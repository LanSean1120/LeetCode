class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        right = 0
        min_sub = nums[0]
        max_sub = nums[0]
        ans = 1

        while right <len(nums):
            if max_sub>min_sub+limit:
                left += 1
                right +=1
                min_sub = min(nums[left:right+1])
                max_sub = max(nums[left:right+1])
                continue
                
            if abs(nums[right]-min_sub)<=limit and abs(nums[right]-max_sub)<=limit:
                min_sub = min(min_sub, nums[right])
                max_sub = max(max_sub, nums[right])
                ans = max(ans, right-left+1)
                right +=1
            else:
                left +=1
                right +=1
                min_sub = min(nums[left:right+1])
                max_sub = max(nums[left:right+1])
        
        return ans




