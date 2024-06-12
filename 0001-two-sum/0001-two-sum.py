class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)

        for i in range(len(nums)):
            if target-nums[i] in d and target-nums[i]!=nums[i]:
                return [i,d[target-nums[i]][0]]
            elif target-nums[i] in d and target-nums[i]==nums[i] and len(d[nums[i]])>1:
                return d[nums[i]]