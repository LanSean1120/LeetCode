class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        mx = 0
        i=0
        while mx < n:
            if nums !=[]:
                if nums[0]>mx+1:
                    ans+=1
                    mx = 2*mx+1
                else:
                    mx += nums[0]
                    nums.pop(0)
            else:
                ans+=1
                mx = 2*mx+1
        return ans
            
