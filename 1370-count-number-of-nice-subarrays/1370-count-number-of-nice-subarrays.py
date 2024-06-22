class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        

        reversion_array = [0 if nums[i]%2==0 else 1 for i in range(len(nums))]

        if sum(reversion_array)<k:
            return 0
        
        count =0
        count_nums = []
        for i in range(len(reversion_array)):
            if reversion_array[i]==0:
                count +=1
                if i==len(reversion_array)-1:
                    count_nums.append(count)
            else:
                count_nums.append(count)
                count =0
        ans = 0

        for i in range(len(count_nums)-k):
            ans += (count_nums[i]+1)*(count_nums[i+k]+1)
        if reversion_array[-1] == 1:
            ans += count_nums[-k]+1
        return ans


