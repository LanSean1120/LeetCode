class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        
        flip_count = 0
        flips = [0]*len(nums)
        ans =0
        for now in range(len(nums)):
            if now >= k:
                flip_count ^= flips[now-k]
            if nums[now]^flip_count == 0:
                if now > len(nums)-k:
                    return -1
                flip_count ^=1
                flips[now] = 1
                ans+=1
            
        
        return ans
        