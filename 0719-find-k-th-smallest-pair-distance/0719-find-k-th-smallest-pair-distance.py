class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        def check(n):
            count = 0
            left = 0
            right = 1
            while right< len(nums):
                if nums[right] - nums[left] <= n:
                    count += right - left
                    right+=1
                else:
                    left +=1
                if right == left:
                    right+=1

            if count < k:
                return True
            else:
                return False
        
        left = 0
        right = nums[-1] - nums[0]

        while left<right:
            mid = (left+right) //2
            if check(mid):
                left = mid+1
            else:
                right = mid
        return left

