class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        cnt = defaultdict(int)

        def sol(i):
            nonlocal count
            if i==len(nums):
                count +=1
                return 
            sol(i+1)
            if nums[i]+k not in cnt and nums[i]-k not in cnt:
                cnt[nums[i]]+=1
                sol(i+1)
                cnt[nums[i]] -=1
                if cnt[nums[i]] ==0:
                    del cnt[nums[i]]
        sol(0)
        return count-1

