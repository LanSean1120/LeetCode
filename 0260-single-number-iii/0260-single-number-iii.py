class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        i=0
        nums.sort()
        while len(ans)<2:
            if i==len(nums)-1:
                ans.append(nums[i])
                break
            if nums[i] == nums[i+1]:
                i+=2
            else:
                ans.append(nums[i])
                i+=1
        return ans
        