class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        ans = nums[0]+nums[1]+nums[2]
        if ans == target:
            return ans

        for i in range(len(nums)-2):
            j=i+1
            n=len(nums)-1
            while j<n:
                sums = nums[i]+nums[j]+nums[n]
                if sums == target:
                    ans = sums
                    break
                elif sums >= ans and ans > target:
                    n-=1
                elif sums <ans and sums > target:
                    ans = sums
                    n-=1
                elif sums <= ans and ans < target:
                    j+=1
                elif sums > ans and sums < target:
                    ans = sums
                    j+=1
                elif sums < target and abs(sums-target)>=abs(ans-target):
                    j+=1
                elif sums < target and abs(sums-target)<abs(ans-target):
                    ans = sums
                    j+=1
                elif sums > target and abs(sums-target)>=abs(ans-target):
                    n-=1
                else:
                    ans = sums
                    n-=1
        return ans
        